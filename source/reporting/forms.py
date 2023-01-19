from django import forms
from reporting.models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['event_date', 'title', 'students_name', 'other', 'teachers_name', 'stage', 'direction', 'subject', 'school_сlass', 'result', 'school_parallel']
        widgets = {'event_date': forms.DateInput(attrs={'placeholder': '19.01.2023',})}