from django.urls import path
from django.views.generic.base import TemplateView
from user import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login$', views.Users.login_view),
    url(r'^register$', views.Users.register_view),
    url(r'^logout$', views.Users.logout_view)
]
