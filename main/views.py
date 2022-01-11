from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail
from .forms import UserForm

from datetime import datetime
import datetime as dt
import requests

from app_user.models import *





def IndexView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "main/index.html", context )



def AboutView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "main/index.html", context )



def ContactView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "main/index.html", context )




def SignUpView(request):

		if request.method == "POST":

			form = UserForm(request.POST or None, request.FILES or None)
			email = request.POST.get("username")
			password1 = "0000"
			password2 = "0000"


			if password1 != password2:
				messages.warning(request, "Make sure both passwords match")
				return HttpResponseRedirect(reverse("main:sign_up"))

				
			else:
				try:
					AppUser.objects.get(user__email=request.POST.get("username"))
					messages.warning(request, "Phone Number already taken, try another one!")
					return HttpResponseRedirect(reverse("main:sign_up"))


				except:
					user = form.save()
					user.set_password(password1)
					user.save()

					app_user = AppUser.objects.create(user=user)
					app_user.save()

					if user:
						if user.is_active:
							login(request, user)

							app_user = AppUser.objects.get(user__pk=request.user.id)
							messages.warning(request, "Welcome, complete your profile!")
							return HttpResponseRedirect(reverse("app_user:profile"))

		else:
			form = UserForm()
			context = {"form": form}
			return render(request, "main/sign_up.html", context )



def SignInView(request):

	if request.method == "POST":
		username = request.POST.get("username")
		password = "0000"

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)

				app_user = AppUser.objects.get(user__pk=request.user.id)

				print("11111111111111111111111111111111")
				messages.success(request, "Welcome Onboard")
				return HttpResponseRedirect(reverse("app_user:index"))
			else:
				print("22222222222222222222222222222222")
				messages.warning(request, "Sorry, Invalid Login Details")
				return HttpResponseRedirect(reverse("main:sign_in"))

		else:
			print("33333333333333333333333333333333333333")
			messages.warning(request, "Sorry, Invalid Login Details")
			return HttpResponseRedirect(reverse("main:sign_in"))



	else:
		context = {}
		return render(request, "main/sign_in.html", context )


