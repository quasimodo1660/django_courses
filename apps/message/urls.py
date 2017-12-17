from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.show),
    url(r'^add$', views.add_message),
    url(r'^udmsg$', views.udate_message),
    url(r'^rmmsg$', views.remove_message),
    url(r'^addcom$', views.add_comment),
]