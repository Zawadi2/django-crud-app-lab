from django import forms
from .models import Recommendation

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['date', 'book','recommends','reason']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
