from django.db.models import Q
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer


class ContactApp(TemplateView):
    """View in charge of serving the contact app and injecting in the context the contact list initial url.
    All the frontend is handled using Vue from this point
    """
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
    Returns a list of persons

    retrieve:
    Returns a single person by id

    create:
    Creates a new person

    update:
    Updates the person that has the provided url id

    partial_update:
    Updates partially the person that has the provided url id

    destroy:
    Removes a person from the db
    """
    serializer_class = PersonSerializer

    def get_queryset(self):
        """Allows to do search queries for all the person attributes and related info"""
        queryset = Person.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(first_name__istartswith=query) | Q(last_name__istartswith=query) | Q(date_of_birth__istartswith=query)
                | Q(email_set__email__istartswith=query) | Q(phonenumber_set__number__istartswith=query)
                | Q(address_set__name__istartswith=query)
            ).distinct()
        return queryset
