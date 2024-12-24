from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label="First Name")
    last_name = forms.CharField(max_length=50, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(max_length=100, required=True, label="Subject")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Message")
