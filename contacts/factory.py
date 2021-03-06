import random

import factory

from . import models


def random_choice(choices_object):
    """Returns a random choice from a choice object"""
    flat_choices_values = [choice[0] for choice in choices_object]
    return random.choice(flat_choices_values)


class EmailFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    info_type = factory.LazyFunction(lambda: random_choice(models.Email.EMAIL_TYPES))

    class Meta:
        model = models.Email


class AddressFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('address')
    info_type = factory.LazyFunction(lambda: random_choice(models.Address.ADDRESS_TYPES))

    class Meta:
        model = models.Address


class PhoneNumberFactory(factory.django.DjangoModelFactory):
    number = factory.LazyFunction(lambda: f"+58424{''.join(str(random.randrange(10)) for _ in range(7))}")
    info_type = factory.LazyFunction(lambda: random_choice(models.PhoneNumber.PHONE_NUMBER_TYPE))

    class Meta:
        model = models.PhoneNumber


class PersonFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_of_birth = factory.Faker('past_date', start_date='-100y')

    class Meta:
        model = models.Person


class PersonWithInfoFactory(PersonFactory):

    @factory.post_generation
    def create_associated_info(self, created, *args, **kwargs):
        if not created:
            return

        def _create_info(info_factory):
            # Creating the info records
            records = info_factory.create_batch(random.randrange(5), person=self)
            if records:
                primary_info = random.choice(records)
                primary_info.primary = True
                primary_info.save()

        _create_info(EmailFactory)
        _create_info(PhoneNumberFactory)
        _create_info(AddressFactory)
