from django.conf.urls import url
from . import views

app_name = 'profiles'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
]