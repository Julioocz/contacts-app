from django.db.models import Q
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer


class ContactApp(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        """Adds the contacts endpoint url to the template context"""
        context = super().get_context_data(**kwargs)
        context['url_contacts'] = reverse('contacts:contact-list')
        return context


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
    serializer_class = PersonSerializer

    def get_queryset(self):
        """Allows to do search queries"""
        queryset = Person.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(first_name__istartswith=query) | Q(last_name__istartswith=query) | Q(date_of_birth__istartswith=query)
                | Q(email_set__email__istartswith=query) | Q(phonenumber_set__number__istartswith=query)
                | Q(address_set__name__istartswith=query)
            ).distinct()
        return queryset
