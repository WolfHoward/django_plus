from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Profile
	

class IndexView(generic.ListView):
	template_name = 'profiles/index.html'
	context_object_name = 'profile_list'

	def get_queryset(self):
		"""Return list of profiles ordered by primary key"""
		return Profile.objects.order_by('-pk')

# def index(request):
# 	profile_list = Profile.objects.order_by('-pk')[:5]
# 	context = {'profile_list': profile_list}

# 	return render(request, 'profiles/index.html', context)

def profile(request, user_id):

	profile = get_object_or_404(Profile, pk=user_id)

	context = {
		'first_name': profile.first_name,
		'last_name': profile.last_name,
		'username': profile.username,
		'email': profile.email,
		'join_date': profile.join_date,
		'discipline': profile.discipline,
		'paired': profile.paired,
	}

	return render(request, 'profiles/profile.html', context)