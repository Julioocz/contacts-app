from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from . import models


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    primary_email = serializers.EmailField(many=False, read_only=True, allow_blank=True, source='get_primary_email')
    primary_address = serializers.CharField(many=False, read_only=True, allow_blank=True, source='get_primary_address')
    primary_phone_number = PhoneNumberField(many=False,
                                            read_only=True,
                                            allow_blank=True,
                                            source='get_primary_phone_number')

    class Meta:
        model = models.Person
        depth = 0
