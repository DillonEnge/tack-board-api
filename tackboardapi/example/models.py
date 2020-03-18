import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
	user_name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	created_at = models.DateTimeField('date created')
	
	def __str__(self):
		return self.user_name

	def was_created_recently(self):
		return self.created_at >= timezone.now() - datetime.timedelta(days=1)