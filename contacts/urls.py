from django.conf.urls import url
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from . import views

router = SimpleRouter()
router.register(r'contacts', viewset=views.PersonViewSet, base_name='person')
person_router = routers.NestedSimpleRouter(router, r'contacts', lookup='person')
person_router.register(r'emails', views.EmailViewSet, base_name='email')
person_router.register(r'addresses', views.AddressViewSet, base_name='address')
person_router.register(r'numbers', views.EmailViewSet, base_name='phone_number')

app_name = 'contacts'
urlpatterns = [
    url('', include(router.urls)),
    url('', include(person_router.urls))
]

