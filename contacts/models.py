from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from model_utils import Choices

from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class Person(TimeStampedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('contacts:contact-detail', kwargs={'pk': self.pk})

    def _get_primary(self, name, attr_name=None):
        """Returns the primary record of the provided related person info object start name.

        primary records are the ones that have the primary bool set to True

        If no there are non records set as primary, the first of the records is returned.

        If there are not records in the info model. None is returned

        If an attr_name is passed, that attribute name is returned. If the attribute does not exist None is returned

        Related objects are: 'email', 'address', 'phone number'
        Example:
            self._get_primary('email', 'email')  # Should return the email that has primary == True

        """
        related_manager = getattr(self, f'{name}_set')
        try:
            instance = related_manager.get(primary=True)
        except ObjectDoesNotExist:
            instance = related_manager.all().first()

        if attr_name is not None:
            return getattr(instance, attr_name, None)
        return instance

    def get_primary_email(self):
        """Returns the primary email for the person"""
        return self._get_primary('email', attr_name='email')

    def get_primary_phone_number(self):
        """Returns the primary phone number for the person"""
        return self._get_primary('phonenumber', attr_name='number')

    def get_primary_address(self):
        """Returns the primary address for the person"""
        return self._get_primary('address', attr_name='name')


class BasePersonInfo(models.Model):
    detail_viewname = ''

    person = models.ForeignKey(Person, related_name='%(class)s_set', on_delete=models.CASCADE)
    primary = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initial_primary = self.primary

    def get_absolute_url(self):
        return reverse(self.detail_viewname, kwargs={'person_pk': self.person_id, 'pk': self.pk})

    def save(self, *args, **kwargs):
        """Checks the primary attribute in the save method. If the info is primary
        the existing primary info will no longer be primary
        """
        if self._initial_primary != self.primary:
            self.__class__.objects.filter(person_id=self.person_id).exclude(id=self.id).update(primary=False)

        super().save(*args, **kwargs)

    class Meta:
        abstract = True


# Info Types
TYPE_HOME = 'home'
TYPE_WORK = 'work'
TYPE_MOVIL = 'movil'
TYPE_PERSONAL = 'personal'
TYPE_OTHER = 'other'


class Email(BasePersonInfo):
    detail_viewname = 'contacts:email-detail'

    EMAIL_TYPES = Choices(TYPE_PERSONAL, TYPE_HOME, TYPE_WORK, TYPE_OTHER)

    email = models.EmailField()
    info_type = models.CharField(max_length=255, choices=EMAIL_TYPES, default=TYPE_PERSONAL)


class Address(BasePersonInfo):
    detail_viewname = 'contacts:address-detail'

    ADDRESS_TYPES = Choices(TYPE_HOME, TYPE_WORK, TYPE_OTHER)

    name = models.CharField(max_length=255)
    info_type = models.CharField(max_length=255, choices=ADDRESS_TYPES, default=TYPE_HOME)


class PhoneNumber(BasePersonInfo):
    detail_viewname = 'contacts:phone_number-detail'

    PHONE_NUMBER_TYPE = Choices(TYPE_MOVIL, TYPE_HOME, TYPE_WORK, TYPE_OTHER)

    number = PhoneNumberField()
    info_type = models.CharField(max_length=255, choices=PHONE_NUMBER_TYPE, default=TYPE_MOVIL)
