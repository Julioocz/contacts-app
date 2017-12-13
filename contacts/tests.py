from django.test import TestCase

from .factory import PersonFactory

class TestFactory(TestCase):
    def test_factory(self):
        person = PersonFactory()
        assert person.first_name
        assert person.last_name
        assert person.date_of_birth

