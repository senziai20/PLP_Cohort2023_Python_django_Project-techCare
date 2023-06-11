# techcare_app/forms.py

from django import forms
from .models import RepairRequest


class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = '__all__'
