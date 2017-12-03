from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from . import models


class URLMixin(serializers.Serializer):
    url = serializers.URLField(source='get_absolute_url')


class EmailSerializer(URLMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Email
        exclude = 'id',


class AddressSerializer(URLMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude = 'id',


class PhoneNumberSerializer(URLMixin, serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = '__all__'


class ListPersonSerializer(URLMixin, serializers.ModelSerializer):
    primary_email = serializers.EmailField(read_only=True, allow_blank=True, source='get_primary_email')
    primary_address = serializers.CharField(read_only=True, allow_blank=True, source='get_primary_address')
    primary_phone_number = PhoneNumberField(read_only=True, allow_blank=True, source='get_primary_phone_number')

    class Meta:
        model = models.Person
        fields = ('url', 'first_name', 'last_name', 'date_of_birth',
                  'primary_email', 'primary_address', 'primary_phone_number')


class DetailPersonSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(source='email_set', many=True)
    phone_numbers = PhoneNumberSerializer(source='phonenumber_set', many=True)
    addresses = AddressSerializer(source='address_set', many=True)

    class Meta:
        model = models.Person
        fields = '__all__'
