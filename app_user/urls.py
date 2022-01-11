from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("profile/", views.ProfileView, name="profile"),

	path("find-phc/", views.FindPhcView, name="find_phc"),
	path("ovulation/", views.OvulationView, name="ovulation"),

	path("edd/", views.EddView, name="edd"),
	path("edd/lp/", views.EddLpView, name="edd_lp"),
	path("edd/cd/", views.EddCdView, name="edd_cd"),
	path("edd/dd/", views.EddDdView, name="edd_dd"),

	path("prams/", views.PramsView, name="prams"),
	path("bmi/", views.BmiView, name="bmi"),
	path("requet_call/", views.RequestCallView, name="requet_call"),
	path("chat/", views.ChatView, name="chat"),

	path("logout/", views.LogoutView, name="logout"),

]