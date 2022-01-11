from django.urls import path
from . import views

app_name = "admin_user"

urlpatterns = [

	path("", views.ManageAllUserView, name="manage_all_users"),

	path("manage-all-phcs/", views.ManageAllPhcsView, name="manage_all_phcs"),
	path("add-phc/", views.AddPhcView, name="add_phc"),

	path("manage-all-contacts/", views.ManageAllContactsView, name="manage_all_contacts"),
	path("add-contact/", views.AddContactView, name="add_contact"),

	path("manage-all-prams/", views.ManageAllPramsView, name="manage_all_prams"),

]