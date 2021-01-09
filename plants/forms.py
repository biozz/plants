from django import forms

from .models import Plant


class PlantAdminForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ()
        widgets = {
            "name": forms.Textarea(attrs={"rows": 1, "cols": 60}),
            "name_lat": forms.Textarea(attrs={"rows": 1, "cols": 60}),
            "name_alt": forms.Textarea(attrs={"rows": 1, "cols": 60}),
            "name_en": forms.Textarea(attrs={"rows": 1, "cols": 60}),
        }
