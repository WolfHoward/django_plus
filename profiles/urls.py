from django.conf.urls import url
from . import views

app_name = 'profiles'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
]