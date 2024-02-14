from django.shortcuts import render
from web.forms import ContactForm, EnquiryForm
from django.http import JsonResponse
from django.shortcuts import render,redirect

from .models import News,Team

def index(request):
    news = News.objects.all()[:3]
    
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
            return JsonResponse(response_data)
        else:
            print(form.errors)
            response_data = {"status": "false", "title": "Form validation error"}
            return JsonResponse(response_data)

    else:
        form = EnquiryForm() 
        context = {
            "is_contact": True,
            "form": form,
            "news":news,
        }
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)


def business_lines(request):
    context = {"is_business_lines": True}
    return render(request, "web/business_lines.html", context)


def team(request):
    team = Team.objects.all()
    context = {"is_team": True,"team":team,}
    return render(request, "web/team.html", context)


def news(request):
    news = News.objects.all()
    context = {"is_news": True,"news":news,}
    return render(request, "web/news.html", context)


def news_details(request):
    context = {"is_news_details": True}
    return render(request, "web/news_details.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
            return JsonResponse(response_data)
        else:
            print(form.errors)
            response_data = {"status": "false", "title": "Form validation error"}
            return JsonResponse(response_data)

    else:
        form = ContactForm() 
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)