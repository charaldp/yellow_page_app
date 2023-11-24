from django import forms

class ContactForm(forms.Form):
    contact_number = forms.CharField(label="Contact Number", max_length=100)
    