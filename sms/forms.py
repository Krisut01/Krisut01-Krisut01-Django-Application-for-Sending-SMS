from django import forms

class SMSForm(forms.Form):
    recipient = forms.CharField(max_length=15, label="Phone Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")
