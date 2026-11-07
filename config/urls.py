from django.contrib import admin
from django.urls import path
from core import views
from enquiries import views as enquiry_views

urlpatterns = [
    path("sarvo-logIN_FR", admin.site.urls),
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("divisions/", views.divisions, name="divisions"),
    path("projects/", views.projects, name="projects"),
    path("about/", views.about, name="about"),
    path("contact/", enquiry_views.contact, name="contact"),
    path("privacy/", views.privacy, name="privacy"),
    path(
        "project/<slug:slug>/",
        views.project_detail,
        name="project_detail"
    ),
]