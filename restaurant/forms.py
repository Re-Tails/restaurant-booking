from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms import DateTimeField
from django.conf import settings

from restaurant.models import Employee, Customer, Reservation

from restaurant.models import Employee, Customer


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=75, required=True)
    address = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'address',
            'password1',
            'password2'
        )
    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class reservationForm(forms.ModelForm):
    '''
    RS_End = DateTimeField(
        widget=forms.DateTimeInput(format=settings.DATETIME_INPUT_FORMATS, attrs={'class':'form-control', 'type':'datetime-local'})
    )
    RS_Start = DateTimeField(
        widget=forms.DateTimeInput(format=settings.DATETIME_INPUT_FORMATS, attrs={'class':'form-control', 'type':'datetime-local'})
    )
    '''
    class Meta:
        model = Reservation
        fields = ['RS_TA', 'RS_People', 'RS_Start', 'RS_End']
        widgets = {
        }
