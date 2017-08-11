from django.db import models
from django.utils import timezone

class Profile(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50, unique=True)
	email = models.CharField(max_length=50, unique=True)
	join_date = models.DateTimeField('date joined')
	discipline = models.CharField(max_length=25, blank=True)
	paired = models.BooleanField(default=False)

	def __str__(self):
		full_name = [self.first_name, self.last_name, str(self.pk)]
		name = ' '.join(full_name)

		return name