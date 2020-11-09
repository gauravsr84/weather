from django import forms

class LoginForm(forms.Form):
    email_id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)