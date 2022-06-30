from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type = "date"

class StudentRecordForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput())

    class Meta:
        model = models.StudentRecord
        fields = "__all__"
