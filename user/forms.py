from django import forms
from django.contrib.auth import password_validation
from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.views import get_user_model

from .models import Wallet


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'uk-input',
                                                           'placeholder': 'UserName'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'uk-input', 'placeholder': 'PassWord'}),
    )


class RegisterForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'uk-input',
                                                           'placeholder': 'UserName'}))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'uk-input', 'placeholder': 'PassWord'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'uk-input', 'placeholder': 'Password confirmation'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    address = forms.CharField(
        label="address",
        widget=forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'address'}),
    )
    phone = forms.CharField(
        label="phone",
        widget=forms.TextInput(attrs={'class': 'uk-input', 'placeholder': 'phone'}),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
            Wallet.objects.create(user=user)
        return user

    class Meta:
        model = get_user_model()
        fields = ['username']
