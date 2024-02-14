from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("team/", views.team, name="team"),
    path("business_lines/", views.business_lines, name="business_lines"),
    path("news/", views.news, name="news"),
    path("contact/", views.contact, name="contact"),
    path("news/<str:slug>/", views.news_details, name="news_details"),
]