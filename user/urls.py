from django.urls import path
from django.views.generic.base import TemplateView
from user import views
from django.conf.urls import url

urlpatterns = [
    url(r'^user/login/$', views.login_view),
    url(r'^get_data/$', views.get_data),
]
