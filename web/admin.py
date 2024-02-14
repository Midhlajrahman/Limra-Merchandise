from django.contrib import admin

from .models import BusinessLines, Team, News, Contact, Enquiry
# Register your models here.

@admin. register(BusinessLines)
class BusinessLinesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin. register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
@admin. register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
@admin. register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
@admin. register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name",)