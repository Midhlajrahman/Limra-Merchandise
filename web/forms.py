from django import forms
from django.forms import widgets

from .models import Contact, Enquiry
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required", "placeholder": "Your Name *"}
            ),
            "number": widgets.NumberInput(
                attrs={"class": "required", "placeholder": "Your Number *"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "required", "placeholder": "Your Email *"}
            ),
            "subject": widgets.TextInput(
                attrs={"class": "required", "placeholder": "Your Subject *"}
            ),
            "message": widgets.Textarea(
                attrs={"class": "required contact-textarea", "placeholder": "Message", "cols": "40", "rows": "4"}
            ),
        }
        

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required", "placeholder": "Your Name *"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "required", "placeholder": "Your Email *"}
            ),
            "subject": widgets.TextInput(
                attrs={"class": "required", "placeholder": "Your Subject *"}
            ),
            "message": widgets.Textarea(
                attrs={"class": "required contact-textarea", "placeholder": "Message", "cols": "40", "rows": "4"}
            ),
        }
