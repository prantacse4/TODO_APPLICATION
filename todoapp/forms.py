from django.core import validators
from django import forms
from todoapp.models import Notes
from django.core.exceptions import ValidationError

#LoginSignup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =[ 'username', 'email', 'password1', 'password2']


class NoteRegistration(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [ 'title', 'note', 'archive', 'date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        for instance in Notes.objects.all():
            if instance.title == title:
                raise forms.ValidationError("একই নামে মাত্র একটি নোট যুক্ত করতে পারবেন")
     
        return title

class NoteRegistrationArchive(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['archive']


class NoteRegistrationUpdate(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note']