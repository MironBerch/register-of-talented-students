from django import forms
from reporting.models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('event_date', 'title', 'student', 'other', 'teachers_name', 'stage', 'direction', 'subject', 'result', 'scan_diploma',)
        widgets = {
            'event_date': forms.DateInput(
                attrs={
                    'placeholder': '19.01.2023',
                }
            ),
            'scan_diploma': forms.FileInput(
                attrs={
                    'id': 'formFile',
                    'type': 'file',
                }
            ),
        }