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

    class Meta:
        ordering = ('-modified', )

    def get_absolute_url(self):
        return reverse('contacts:contact-detail', kwargs={'pk': self.pk})


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
        ordering = ('-primary',)


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

    PHONE_NUMBER_TYPE = Choices(TYPE_MOVIL, TYPE_PERSONAL, TYPE_HOME, TYPE_WORK, TYPE_OTHER)

    number = PhoneNumberField()
    info_type = models.CharField(max_length=255, choices=PHONE_NUMBER_TYPE, default=TYPE_MOVIL)
