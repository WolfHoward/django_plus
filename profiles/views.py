from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("This is the profile index.")

def profile(request, user_id):
	context = {
		'first_name': user_id.first_name,
		'last_name': user_id.last_name,
	}
	return HttpResponse("You're looking at user #%s." % user_id)