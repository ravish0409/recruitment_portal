 
from django import forms
from .models import Candidate

from django import forms
from .models import Candidate

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'skills', 'experience']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your skills'}),
            'experience': forms.Select(attrs={'class': 'form-control'})
        }

    
class JobSearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter location'
    }))
    skills = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter skills'
    }))
    experience = forms.ChoiceField(
        choices=[
            ('', 'Any'),
            ('entry level', 'Entry Level'),
            ('mid level', 'Mid Level'),
            ('senior level', 'Senior Level'),
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )