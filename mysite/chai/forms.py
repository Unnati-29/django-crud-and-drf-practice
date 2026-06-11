from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(
        queryset=ChaiVariety.objects.all(),
        label="Select Chai Variety",
        widget=forms.Select(
            attrs={
                "class": "w-full bg-slate-800 border border-slate-600 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-amber-500"
            }
        )
    )