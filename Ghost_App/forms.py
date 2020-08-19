from django import forms

class BoastOrRoastForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    is_boast = forms.BooleanField(required=False)