from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.auth, name='auth'),
    url(r'^main/$', views.main, name='main'),
    url(r'^info/(?P<pk>[0-9]+)$', views.info, name='info'),
    url(r'^edit/$', views.edit, name='edit'),
]
