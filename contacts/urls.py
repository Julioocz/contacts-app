from django.conf.urls import url
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from . import views

router = SimpleRouter()
router.register(r'contacts', viewset=views.PersonViewSet, base_name='contact')

app_name = 'contacts'
urlpatterns = [
    path('', view=views.ContactApp.as_view(), name='app'),
    url('', include(router.urls)),
]

