from django.urls import path
from . import views



app_name = "website"

urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("contact/",views.ContactView.as_view(),name="contact"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("ticket/", views.SendTicketView.as_view(), name="ticket"),
    path("newsletter/", views.NewsletterView.as_view(), name="newsletter"),
]

