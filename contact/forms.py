from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    contact_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))
    contact_email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    contact_message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Message'}))
    
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message']
