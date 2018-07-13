from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.register),
    url(r'register', views.register),
    url(r'login', views.login),
    url(r'users/new', views.register),
    url(r'users', views.users),
]