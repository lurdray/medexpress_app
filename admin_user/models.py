from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Phc(models.Model):
	name = models.CharField(default="",max_length=20)
	location = models.TextField(default="")
	contact = models.CharField(default="",max_length=20)

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name




class Contact(models.Model):
	name = models.CharField(default="",max_length=20)
	spec = models.CharField(default="",max_length=20)
	location = models.TextField(default="")
	phone = models.CharField(default="",max_length=20)
	whatsapp = models.CharField(default="",max_length=20)
	email = models.CharField(default="",max_length=20)

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name