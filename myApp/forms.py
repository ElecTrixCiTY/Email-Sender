
from django import forms
from django.core.validators import validate_email





class EmailForm(forms.Form):
    subject = forms.CharField()
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


def validateEmail(recipient):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(recipient)
        return True
    except ValidationError:
        return False
