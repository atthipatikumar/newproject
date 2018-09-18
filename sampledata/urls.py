from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register1, name='register1'),
    url(r'^$', views.login1, name='login1'),
]