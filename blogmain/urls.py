from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^timeaxis$', views.get_timeaxis),
]