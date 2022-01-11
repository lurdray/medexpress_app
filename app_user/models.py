from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_photo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.png")

	name = models.CharField(default="",max_length=20)
	age = models.CharField(default="",max_length=20)
	address = models.TextField(default="")
	pregnancy_status = models.CharField(default="",max_length=20)
	blood_group = models.CharField(default="",max_length=20)
	hiv_status = models.CharField(default="",max_length=20)

	last_bmi = models.CharField(default="",max_length=20)
	last_edd = models.CharField(default="",max_length=20)
	last_ovulation = models.CharField(default="",max_length=20)

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username




class PramData(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

	hypertension = models.CharField(default="",max_length=20)
	diabetes = models.CharField(default="",max_length=20)
	asthma = models.CharField(default="",max_length=20)
	seizure = models.CharField(default="",max_length=20)
	kidney = models.CharField(default="",max_length=20)
	systemic = models.CharField(default="",max_length=20)
	hiv = models.CharField(default="",max_length=20)
	heart = models.CharField(default="",max_length=20)
	cancer = models.CharField(default="",max_length=20)
	brain = models.CharField(default="",max_length=20)
	hypothyroidism = models.CharField(default="",max_length=20)
	hyperthyroidism = models.CharField(default="",max_length=20)
	clotting = models.CharField(default="",max_length=20)
	preeclampsia_prior = models.CharField(default="",max_length=20)
	preeclampsia_after = models.CharField(default="",max_length=20)
	preterm_delivery = models.CharField(default="",max_length=20)
	preterm_delivery_prior = models.CharField(default="",max_length=20)
	rupture = models.CharField(default="",max_length=20)
	cerclage = models.CharField(default="",max_length=20)
	uterine = models.CharField(default="",max_length=20)
	stillbirth = models.CharField(default="",max_length=20)
	intrauterine = models.CharField(default="",max_length=20)
	trimester = models.CharField(default="",max_length=20)
	bmi = models.CharField(default="",max_length=20)
	oligohydramnios = models.CharField(default="",max_length=20)
	polyhydramnios = models.CharField(default="",max_length=20)
	iugr = models.CharField(default="",max_length=20)
	fetal = models.CharField(default="",max_length=20)
	ivf = models.CharField(default="",max_length=20)
	age_years = models.CharField(default="",max_length=20)
	multiple_gestation = models.CharField(default="",max_length=20)


	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.app_user.name




