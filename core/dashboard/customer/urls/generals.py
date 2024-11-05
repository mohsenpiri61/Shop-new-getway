from django.urls import path, include
from dashboard.customer import views


urlpatterns = [

    path("home/", views.CustomerDashboardHomeView.as_view(), name="home"),
]
