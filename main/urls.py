from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("about/", views.AboutView, name="about"),
	path("contact/", views.ContactView, name="contact"),
	path("sign-up/", views.SignUpView, name="sign_up"),
	path("sign-in/", views.SignInView, name="sign_in"),

]