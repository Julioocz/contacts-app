import random

from django.test import TestCase

from .factory import PersonFactory, EmailFactory, PhoneNumberFactory, AddressFactory


class TestFactory(TestCase):
    def test_factory(self):
        person = PersonFactory()
        assert person.first_name
        assert person.last_name
        assert person.date_of_birth


# Testing models
class TestPrimaryInfo(TestCase):
    def setUp(self):
        self.person = PersonFactory.build()
        self.person.save()

    def _test_primary_info(self, factory_class, comparing_attr, get_primary_method_name):
        primary_info = factory_class.create(primary=True, person_id=self.person.id)
        non_primary_info = factory_class.create_batch(2, person_id=self.person.id)
        assert getattr(self.person, get_primary_method_name)() == getattr(primary_info, comparing_attr)

        # Making another primary info as primary should make the previous one non primary
        next_primary_info = random.choice(non_primary_info)
        next_primary_info.primary = True
        next_primary_info.save()
        new_primary_info_on_person = getattr(self.person, get_primary_method_name)()
        print(new_primary_info_on_person)
        # Checking that the old primary info no longer is
        assert new_primary_info_on_person != getattr(primary_info, comparing_attr)
        assert new_primary_info_on_person == getattr(next_primary_info, comparing_attr)

    def test_get_primary_email(self):
        self._test_primary_info(EmailFactory, 'email', 'get_primary_email')

    def test_get_primary_address(self):
        self._test_primary_info(AddressFactory, 'name', 'get_primary_address')

    def test_get_primary_phone_number(self):
        # Phones are a bit different to test so we do it here
        primary_number = PhoneNumberFactory(number='+584241234567', person_id=self.person.id)
        non_primary_number = PhoneNumberFactory(number='+14155552671', person_id=self.person.id)
        assert self.person.get_primary_phone_number() == primary_number.number
        non_primary_number.primary = True
        non_primary_number.save()
        assert self.person.get_primary_phone_number() != primary_number.number
        assert self.person.get_primary_phone_number() == non_primary_number.number
