from django.db import models
from django.contrib.auth.models import User
import datetime

class QuestionManager(models.Manager):

	def popular(self):
		return self.get_queryset().order_by('-rating')

class Question(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	author = models.ForeignKey(User)
	created = models.DateTimeField(default=datetime.datetime.now)
	rating = models.IntegerField(default=0)	

	objects = QuestionManager()

	def __unicode__(self):
		return self.title
