from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_postal_data/$', views.get_postal_data, name='get_postal_data'),
]
