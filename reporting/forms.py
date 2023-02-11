from django import forms

from reporting.models import Contest
from students.services import get_learning_students, get_all_classes


class ContestForm(forms.ModelForm):
    school_сlass = forms.ModelChoiceField(
            queryset=get_all_classes(),
    )
    event_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        ),
    )
    student = forms.ModelChoiceField(
            queryset=get_learning_students(),
        )
    class Meta:
        model = Contest
        fields = ('event_date', 'title', 'student', 'other', 'teachers_name', 'stage', 'direction', 'subject', 'result', 'scan_diploma',)
        widgets = {
            'scan_diploma': forms.FileInput(
                attrs={
                    'id': 'formFile',
                    'type': 'file',
                }
            ),
        }     