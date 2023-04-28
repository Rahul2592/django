from django.forms import ModelForm
from ors.models import Marksheet
from django import forms

class MarksheetForm(ModelForm):
    class Meta:
        model=Marksheet
        fields="__all__"
        widgets={
            "rollno":forms.NumberInput(attrs={"class":"form-control", "placeholder":"Enter Rollno"}),
            "name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Name"}),
            "physics":forms.NumberInput(attrs={"class":"form-control", "placeholder":"Enter Physics Score"}),
            "chemistry":forms.NumberInput(attrs={"class":"form-control", "placeholder":"Enter Chemistry Score"}),
            "maths":forms.NumberInput(attrs={"class":"form-control", "placeholder":"Enter Maths Score"}),
        }
