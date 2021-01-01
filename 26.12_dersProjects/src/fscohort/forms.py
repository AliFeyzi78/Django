from django import forms
from django.forms import fields
from .models import Student

# class StudentForm(forms.Form):
# first_name = forms.CharField(max_length=50, label="Name")
# last_name = forms.CharField(max_length=50, label="Surname")
# number = forms.IntegerField()


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label="Name ")

    class Meta:
        model = Student
        fields = "__all__"  # ("first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].label = "MyName"
