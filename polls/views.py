from django.db.models import F
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

# Display 5 most recent questions.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions"""
		if Question.objects.filter(choice=True):
			return Question.objects.filter(
				pub_date__lte=timezone.now(),
				).order_by('-pub_date')[:5]

		#return Question.objects.order_by('-pub_date')[:5]


# Display question and set of choices associated with that question.
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


# Display results of voting
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

# Allow user to submit a vote, which will be recorded to the database.
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	# Check for KeyError, re: 'choice' being passed in a POST request.
	try:
		# request.POST values are returned as a string.
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes = F('votes') + 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back button.
		# Takes a single value, the url to which we're redirecting the user.
		# The reverse function is used to avoid having a hardcoded URL in the view function.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))