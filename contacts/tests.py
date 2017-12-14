import functools
import random

from django.forms import model_to_dict
from django.test import TestCase

from contacts.models import Person
from contacts.serializers import PersonSerializer
from .factory import PersonFactory, AddressFactory, PhoneNumberFactory, EmailFactory, PersonWithInfoFactory


class TestFactory(TestCase):
    def test_factory(self):
        person = PersonFactory()
        assert person.first_name
        assert person.last_name
        assert person.date_of_birth


# Helpers
_model_to_dict = functools.partial(model_to_dict, exclude=['id', 'person'])


def compare_unordered_lists(list1, list2, key, transform_func=None):
    """Compares 2 unordered list of items by sorting them first using the provided key on the sort lambda
    If a transform func is provided it's used on the key func before returning the item value
    """

    def key_func(item):
        value = item[key]
        if transform_func is not None:
            value = transform_func(value)
        return value

    return sorted(list1, key=key_func) == sorted(list2, key=key_func)


def _model_list_to_dict(iterable):
    return list(map(_model_to_dict, iterable))


class TestPersonSerializer(TestCase):
    """Tests both create and update custom methods for the person serializer"""

    def test_create_makes_related_objects(self):
        addresses = AddressFactory.build_batch(random.randint(1, 3))
        phone_numbers = PhoneNumberFactory.build_batch(random.randint(1, 3))
        emails = EmailFactory.build_batch(random.randint(1, 3))
        person = PersonFactory.build()

        person_dict = _model_to_dict(person)
        emails_list = _model_list_to_dict(emails)
        phone_numbers_list = _model_list_to_dict(phone_numbers)
        for phone_number_obj in phone_numbers_list:
            phone_number_obj['number'] = str(phone_number_obj['number'])

        addresses_list = _model_list_to_dict(addresses)
        # Removing None values from the factories
        payload = {
            **person_dict,
            'emails': emails_list,
            'phone_numbers': phone_numbers_list,
            'addresses': addresses_list,
        }

        print(payload)
        serializer = PersonSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        # This should create all the emails, phone numbers and other stuff
        instance = serializer.save()

        # Checking the Person
        assert _model_to_dict(instance) == person_dict
        instance_emails = _model_list_to_dict(instance.email_set.all())
        instance_addresses = _model_list_to_dict(instance.address_set.all())
        instance_phone_numbers = _model_list_to_dict(instance.phonenumber_set.all())
        assert compare_unordered_lists(instance_emails, emails_list, 'email')
        assert compare_unordered_lists(instance_addresses, addresses_list, 'name')
        assert compare_unordered_lists(instance_phone_numbers, phone_numbers_list, 'number', transform_func=str)

    def test_update_updates_creates_and_deletes_related_objects(self):
        person = PersonWithInfoFactory.create()
        test_info_for_adding = _model_to_dict(EmailFactory.build())
        test_info_for_replacing = _model_to_dict(PhoneNumberFactory.build())
        payload = {
            'first_name': person.first_name,
            'last_name': person.last_name,
            'date_of_birth': person.date_of_birth,
            'emails': [*_model_list_to_dict(person.email_set.all()), test_info_for_adding],
            'phone_numbers': [test_info_for_replacing],
            'addresses': []  # Removing,
        }

        initial_email_count = person.email_set.all().count()
        serializer = PersonSerializer(instance=person, data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        person.refresh_from_db()
        assert initial_email_count + 1 == person.email_set.all().count()
        instance_phone_numbers = list(person.phonenumber_set.all())
        assert len(instance_phone_numbers) == 1
        assert _model_to_dict(instance_phone_numbers[0]) == test_info_for_replacing
        assert person.address_set.count() == 0
