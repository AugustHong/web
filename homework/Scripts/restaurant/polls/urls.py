from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<restaurant_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<restaurant_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<restaurant_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^/add_restaurant/$', views.add_restaurant, name='add_restaurant'),
    url(r'^/delete_restaurant/$', views.delete_restaurant, name='delete_restaurant'),
]