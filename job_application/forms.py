from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=15)