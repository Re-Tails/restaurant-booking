from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Order, OrderItem, Item
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=75, required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

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
            'password'
        )

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = (
            'OR_BR',
        )

class AddOrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = (
            'OI_IT',
            'OI_OR',
        )
    OI_IT = forms.ModelChoiceField(queryset = Item.objects.all().filter(IT_CA_id = 1))
