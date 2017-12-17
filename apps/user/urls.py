from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^login/process$', views.loginP),
    url(r'^register/process$', views.regiP),
    url(r'^userinfo', views.show),
]