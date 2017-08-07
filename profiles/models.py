from django.db import models
from django.utils import timezone

class Profile(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	join_date = models.DateTimeField('date joined')

	def __str__(self):
		full_name = [self.first_name, self.last_name, str(self.pk)]
		name = ' '.join(full_name)

		return name