from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    username = forms.CharField(label='Username', widget=forms.TextInput(
                                   attrs={'placeholder': 'Username'})
                                )
    email = forms.EmailField(label='Email', widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'Your e-mail'})
                            )
    firstname = forms.CharField(label='Firstname', widget=forms.TextInput(
                                   attrs={'placeholder': 'Firstname'})
                                )
    lastname = forms.CharField(label='Lastname', widget=forms.TextInput(
                                   attrs={'placeholder': 'Lastname'})
                                )
    password1 = forms.CharField(label='Password', widget=forms.widgets.PasswordInput(
                                    attrs={'placeholder': 'Password'})
                                )
    password2 = forms.CharField(label='Password (again)', widget=forms.widgets.PasswordInput(
                                    attrs={'placeholder': 'Password confirmation'})
                                )

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname',
                  'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in cleaned_data and 'password2' in cleaned_data:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return cleaned_data


class AuthenticationForm(forms.Form):
    """
    Login form
    """
    username = forms.CharField(label='Username', widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'Username'})
                            )
    password = forms.CharField(label='Password', widget=forms.widgets.PasswordInput(
                                    attrs={'placeholder': 'Password'})
                            )

    class Meta:
        fields = ['username', 'password']