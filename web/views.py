from django.shortcuts import render


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)


def business_lines(request):
    context = {"is_business_lines": True}
    return render(request, "web/business_lines.html", context)


def team(request):
    context = {"is_team": True}
    return render(request, "web/team.html", context)


def news(request):
    context = {"is_news": True}
    return render(request, "web/news.html", context)


def news_details(request):
    context = {"is_news_details": True}
    return render(request, "web/news_details.html", context)


def contact(request):
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)