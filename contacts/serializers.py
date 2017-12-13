from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from . import models


class IncludeIDMixin(serializers.Serializer):
    id = serializers.IntegerField(required=False)


class EmailSerializer(IncludeIDMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Email
        exclude = 'person',


class AddressSerializer(IncludeIDMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude = 'person',


class PhoneNumberSerializer(IncludeIDMixin, serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        exclude = 'person',


# Helpers for the person serializer
def _set_dict_to_attrs(obj, dict_obj):
    for prop, value in dict_obj.items():
        setattr(obj, prop, value)


def _update_related(person, model_class, info_list):
    """Modifies the related field to the person object. If the record doesn't exist
    a new one is created
    """
    for item in info_list:
        try:
            record = model_class.objects.filter(person=person).get(id=item.pop('id', None))
        except ObjectDoesNotExist:
            record = model_class(person=person)
        _set_dict_to_attrs(record, item)
        record.save()


def _create_info(person, model_class, info_list):
    """Creates a list of person info objects taking the their data from the info_list arg and using the provided
    model class"""
    objs = [model_class(person=person, **data) for data in info_list]
    model_class.objects.bulk_create(objs)


class PersonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    emails = EmailSerializer(source='email_set', many=True)
    phone_numbers = PhoneNumberSerializer(source='phonenumber_set', many=True)
    addresses = AddressSerializer(source='address_set', many=True)

    class Meta:
        model = models.Person
        fields = '__all__'

    def create(self, validated_data):
        """Creates the associated info type for the person"""
        emails_data = validated_data.pop('email_set')
        phone_numbers_data = validated_data.pop('phonenumber_set')
        addresses_data = validated_data.pop('address_set')
        person = models.Person.objects.create(**validated_data)
        _create_info(person, models.Email, emails_data)
        _create_info(person, models.PhoneNumber, phone_numbers_data)
        _create_info(person, models.Address, addresses_data)
        return person

    def update(self, instance, validated_data):
        """Updates the person object and the related fields"""
        emails_data = validated_data.pop('email_set')
        phone_numbers_data = validated_data.pop('phonenumber_set')
        addresses_data = validated_data.pop('address_set')

        _update_related(instance, models.Email, emails_data)
        _update_related(instance, models.PhoneNumber, phone_numbers_data)
        _update_related(instance, models.Address, addresses_data)
        _set_dict_to_attrs(instance, validated_data)
        instance.save()
        return instance
