from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is success is-medium",
            }
        ),
        label="",
    )

#This options class allows you to pass any information that isn’t a field to your form class.
    class Meta:
        model = Dweet
        exclude = ("user", )