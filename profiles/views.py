from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Profile

def index(request):
	profile_list = Profile.objects.order_by('-pk')[:5]
	context = {'profile_list': profile_list}

	return render(request, 'profiles/index.html', context)

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