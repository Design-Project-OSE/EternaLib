from django import forms

class searchform(forms.Form):
    searchterm = forms.CharField(label='Search words', max_length=100)