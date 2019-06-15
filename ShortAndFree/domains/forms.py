from django import forms

class FilterDomainForm(forms.Form):
    tk = forms.BooleanField(required=False)
    ml = forms.BooleanField(required=False)
    ga = forms.BooleanField(required=False)
    cf = forms.BooleanField(required=False)
    gq = forms.BooleanField(required=False)
