from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

from app_user.models import *
from admin_user.models import *



#from .forms import UserForm


def LogoutView(request):
	pass


def IndexView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/index.html", context )



def ProfileView(request):
	if request.method == "POST":

		phone = request.POST.get("phone")
		name = request.POST.get("name")
		age = request.POST.get("age")
		address = request.POST.get("address")

		pregnancy_status = request.POST.get("pregnancy_status")
		blood_group = request.POST.get("blood_group")
		hiv_status = request.POST.get("hiv_status")

		app_user = AppUser.objects.get(user__pk=request.user.id)
		#app_user.phone = phone
		app_user.name = name
		app_user.age = age
		app_user.address = address

		app_user.pregnancy_status = pregnancy_status
		app_user.blood_group = blood_group
		app_user.hiv_status = hiv_status

		app_user.save()

		return HttpResponseRedirect(reverse("app_user:profile"))


	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "app_user/profile.html", context )



def FindPhcView(request):
	if request.method == "POST":

		location = request.POST.get("location")
		results = Phc.objects.filter(location=location)

		locations = set()

		phcs = Phc.objects.all()
		for item in phcs:
			locations.add(item.location)

		context = {"results": results, "locations": locations}
		return render(request, "app_user/find_phc.html", context )


	else:

		locations = set()

		phcs = Phc.objects.all()
		for item in phcs:
			locations.add(item.location)


		context = {"locations": locations}
		return render(request, "app_user/find_phc.html", context )



def OvulationView(request):
	if request.method == "POST":
		last_period = request.POST.get("last_period")
		cycle = request.POST.get("cycle")

		year = str(last_period[0]) + str(last_period[1]) + str(last_period[2]) + str(last_period[3])
		month = str(last_period[5]) + str(last_period[6])
		day = str(last_period[8]) + str(last_period[9]) 

		datetime_object = datetime.strptime('%s-%s-%s' % (year, month, day), '%Y-%m-%d')
		ovulation_date = datetime.date(datetime_object)+ dt.timedelta(days=14)

		context = {"ovulation_date": ovulation_date}
		return render(request, "app_user/ovulation.html", context )


	else:

		context = {}
		return render(request, "app_user/ovulation.html", context )


def EddView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/edd.html", context )



def EddCdView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/edd_cd.html", context )



def EddDdView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/edd_dd.html", context )



def EddLpView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/edd_lp.html", context )




def PramsView(request):
	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)

		pram_data = PramData.objects.create(app_user=app_user)

		if request.POST.get("hypertension"):
			pram_data.hypertension = request.POST.get("hypertension")

		if request.POST.get("diabetes"):
			pram_data.diabetes = request.POST.get("diabetes")

		if request.POST.get("asthma"):
			pram_data.asthma = request.POST.get("asthma")

		if request.POST.get("seizure"):
			pram_data.seizure = request.POST.get("seizure")

		if request.POST.get("kidney"):
			pram_data.kidney = request.POST.get("kidney")

		if request.POST.get("systemic"):
			pram_data.systemic = request.POST.get("systemic")

		if request.POST.get("hiv"):
			pram_data.hiv = request.POST.get("hiv")

		if request.POST.get("heart"):
			pram_data.heart = request.POST.get("heart")

		if request.POST.get("cancer"):
			pram_data.cancer = request.POST.get("cancer")

		if request.POST.get("brain"):
			pram_data.brain = request.POST.get("brain")

		if request.POST.get("hypothyroidism"):
			pram_data.hypothyroidism = request.POST.get("hypothyroidism")

		if request.POST.get("hyperthyroidism"):
			pram_data.hyperthyroidism = request.POST.get("hyperthyroidism")

		if request.POST.get("clotting"):
			pram_data.clotting = request.POST.get("clotting")

		if request.POST.get("preeclampsia_prior"):
			pram_data.preeclampsia_prior = request.POST.get("preeclampsia_prior")
		
		if request.POST.get("preeclampsia_after"):
			pram_data.preeclampsia_after = request.POST.get("preeclampsia_after")
		
		if request.POST.get("preterm_delivery"):
			pram_data.preterm_delivery = request.POST.get("preterm_delivery")
		
		if request.POST.get("preterm_delivery_prior"):
			pram_data.preterm_delivery_prior = request.POST.get("preterm_delivery_prior")
		
		if request.POST.get("rupture"):
			pram_data.rupture = request.POST.get("rupture")

		if request.POST.get("cerclage"):
			pram_data.cerclage = request.POST.get("cerclage")

		if request.POST.get("uterine"):
			pram_data.uterine = request.POST.get("uterine")

		if request.POST.get("stillbirth"):
			pram_data.stillbirth = request.POST.get("stillbirth")

		if request.POST.get("intrauterine"):
			pram_data.intrauterine = request.POST.get("intrauterine")

		if request.POST.get("trimester"):
			pram_data.trimester = request.POST.get("trimester")

		if request.POST.get("bmi"):
			pram_data.bmi = request.POST.get("bmi")

		if request.POST.get("oligohydramnios"):
			pram_data.oligohydramnios = request.POST.get("oligohydramnios")
		
		if request.POST.get("polyhydramnios"):
			pram_data.polyhydramnios = request.POST.get("polyhydramnios")
		
		if request.POST.get("iugr"):
			pram_data.iugr = request.POST.get("iugr")

		if request.POST.get("fetal"):
			pram_data.fetal = request.POST.get("fetal")

		if request.POST.get("ivf"):
			pram_data.ivf = request.POST.get("ivf")

		if request.POST.get("age"):
			pram_data.age = request.POST.get("age")

		if request.POST.get("multiple_gestation"):
			pram_data.multiple_gestation = request.POST.get("multiple_gestation")

		pram_data.save()



		return HttpResponseRedirect(reverse("app_user:prams"))


	else:
		context = {}
		return render(request, "app_user/prams.html", context )



def BmiView(request):
	if request.method == "POST":
		height = request.POST.get("height")
		weight = request.POST.get("weight")

		bmi = float(float(height)/(float(weight)))

		context = {"bmi": bmi}
		return render(request, "app_user/bmi.html", context )


	else:
		context = {}
		return render(request, "app_user/bmi.html", context )



def RequestCallView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "app_user/index.html", context )



def ChatView(request):

	if request.method == "POST":

		location = request.POST.get("location")
		results = Contact.objects.filter(location=location)

		locations = set()

		contacts = Contact.objects.all()
		for item in contacts:
			locations.add(item.location)


		context = {"results": results, "locations": locations}
		return render(request, "app_user/chat.html", context )


	else:

		locations = set()

		contacts = Contact.objects.all()
		for item in contacts:
			locations.add(item.location)


		context = {"locations": locations}
		return render(request, "app_user/chat.html", context )

