from django.shortcuts import render

from rest_framework import viewsets, mixins

from .serializers import ListPersonSerializer, DetailPersonSerializer, EmailSerializer, AddressSerializer, \
    PhoneNumberSerializer
from .models import Person, Email, Address, PhoneNumber


class PersonViewSet(viewsets.ModelViewSet):
    """
    Viewset for the person objects

    list:
    Return a list of the persons saved with their primary email, address and phone number

    retrieve:
    Return a given person with all its emails, address and phone numbers

    create:
    Creates a new person

    update:
    Updates a person

    partial_update:
    Updates partially a person

    destroy:
    Removes a person from the db
    """
    queryset = Person.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        """Returns the list serializer when no pk an the method is not POST (this conditions are the ones
        for the list view)"""
        if 'pk' not in self.kwargs and not self.request.method == 'POST':
            return ListPersonSerializer

        return DetailPersonSerializer


class BasePersonInfoViewSet(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    """Base view set for the persons info"""
    model = None

    def get_queryset(self):
        return self.model.objects.filter(person_id=self.kwargs['person_pk'])


class EmailViewSet(BasePersonInfoViewSet):
    serializer_class = EmailSerializer
    model = Email


class AddressViewSet(BasePersonInfoViewSet):
    serializer_class = AddressSerializer
    model = Address


class PhoneNumberViewSet(BasePersonInfoViewSet):
    serializer_class = PhoneNumberSerializer
    model = PhoneNumber
