from datetime import date, timedelta
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name', 'last_name', 'job_title',
            'company', 'email', 'linkedin',
            'add_contact', 'group', 'last_contact', 'next_contact',
            'status', 'step', 'comment', 'history',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'linkedin': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'group': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'add_contact': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8, 'cols': 10,
            }),
            'last_contact': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'next_contact': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'step': forms.Select(attrs={
                'class': 'form-select',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5, 'cols': 15,
            }),
            'history': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5, 'cols': 15,
            }),
        }

    def clean_next_contact(self):
        next_contact = self.cleaned_data['next_contact']

        if next_contact < date.today():
            raise forms.ValidationError("Вы не можете создать дату следующего контакта, позже сегодняшнего дня!")

        return next_contact
