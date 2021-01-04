from django.core import validators
from django import forms
from todoapp.models import Notes
from django.core.exceptions import ValidationError

class NoteRegistration(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'note', 'archive']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        for instance in Notes.objects.all():
            if instance.title == title:
                raise forms.ValidationError("Note Already Exists")
     
        return title

class NoteRegistrationArchive(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['archive']