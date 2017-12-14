from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .utils import set_dict_to_attrs
from . import models


class IncludeIDMixin(serializers.Serializer):
    """
    This is used to allow to include the id for related object serializers -- allowing to update the objects using
    the PersonSerializer
    """
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
def _update_related(person, model_class, info_list):
    """Modifies the related field to the person object. If the record doesn't exist
    a new one is created
    """
    # Removing removed related objects
    info_ids = [info['id'] for info in info_list if 'id' in info]
    model_class.objects.filter(person=person).exclude(id__in=info_ids).delete()

    # Adding new info and updating existent
    for item in info_list:
        try:
            record = model_class.objects.filter(person=person).get(id=item.pop('id', None))
        except ObjectDoesNotExist:
            record = model_class(person=person)
        set_dict_to_attrs(record, item)
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
        """Creates the associated info (email, phone number, address) for the person.
        Overriding this method allows to handle the person object creation and its related info in a single serializer
        """
        emails_data = validated_data.pop('email_set')
        phone_numbers_data = validated_data.pop('phonenumber_set')
        addresses_data = validated_data.pop('address_set')
        person = models.Person.objects.create(**validated_data)
        _create_info(person, models.Email, emails_data)
        _create_info(person, models.PhoneNumber, phone_numbers_data)
        _create_info(person, models.Address, addresses_data)
        return person

    def update(self, instance, validated_data):
        """Updates the person object and the related fields.
        Overriding this method allows to hanlde the person object update and its related info in a single serializer.

        NOTE: All the related object serialzers must inherit from IncludeIDMixin to them to take the related object
        id
        """
        emails_data = validated_data.pop('email_set')
        phone_numbers_data = validated_data.pop('phonenumber_set')
        addresses_data = validated_data.pop('address_set')

        _update_related(instance, models.Email, emails_data)
        _update_related(instance, models.PhoneNumber, phone_numbers_data)
        _update_related(instance, models.Address, addresses_data)
        set_dict_to_attrs(instance, validated_data)
        instance.save()
        return instance
