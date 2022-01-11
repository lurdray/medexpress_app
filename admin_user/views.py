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






def IndexView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "admin_user/index.html", context )



def ManageAllUserView(request):
	if request.method == "POST":
		pass


	else:
		app_users = AppUser.objects.order_by('-pub_date')

		context = {"app_users": app_users}
		return render(request, "admin_user/manage_all_users.html", context )






def ManageAllPramsView(request):
	if request.method == "POST":
		pass


	else:

		prams = PramData.objects.order_by('-pub_date')

		context = {"prams": prams}
		return render(request, "admin_user/manage_all_prams.html", context )






def ManageAllContactsView(request):
	if request.method == "POST":
		pass


	else:
		contacts = Contact.objects.order_by('-pub_date')

		context = {"contacts": contacts}
		return render(request, "admin_user/manage_all_contacts.html", context )



def AddContactView(request):
	if request.method == "POST":

		spec = request.POST.get("spec")
		name = request.POST.get("name")
		location = request.POST.get("location")
		phone = request.POST.get("phone")
		whatsapp = request.POST.get("whatsapp")
		email = request.POST.get("email")



		contact_model = Contact.objects.create(spec=spec, name=name, location=location, phone=phone, whatsapp=whatsapp, email=email)
		contact_model.save()

		return HttpResponseRedirect(reverse("admin_user:manage_all_contacts"))


	else:
		context = {}
		return render(request, "admin_user/add_contact.html", context )





def AddPhcView(request):
	if request.method == "POST":

		name = request.POST.get("name")
		location = request.POST.get("location")
		contact = request.POST.get("contact")

		phc_model = Phc.objects.create(name=name, location=location, contact=contact)
		phc_model.save()

		return HttpResponseRedirect(reverse("admin_user:manage_all_phcs"))


	else:
		context = {}
		return render(request, "admin_user/add_phc.html", context )





def ManageAllPhcsView(request):
	if request.method == "POST":
		pass



	else:
		phcs = Phc.objects.order_by('-pub_date')

		context = {"phcs": phcs}
		return render(request, "admin_user/manage_all_phcs.html", context )



