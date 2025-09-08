from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label='Full Name',
        help_text='Enter your full name.'
    )
    
    email = forms.EmailField(
        label='Email Address',
        help_text='Enter a valid email address.'
    )
    
    phone_number = forms.CharField(
        max_length=15,
        label='Phone Number',
        help_text='Enter a valid phone number including country code, e.g., +1234567890',
        validators=[
            RegexValidator(regex=r'^\+?1?\d{9,15}$',
                           message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.')
        ]
    )
    
    national_id = forms.CharField(
        max_length=20,
        label='National ID',
        help_text='Enter your national identification number or ID card number.'
    )
    
    username = forms.CharField(
        max_length=50,
        label='Username',
        help_text='Enter your desired username.'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',
        help_text='Enter a secure password.'
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password',
        help_text='Re-enter your password for confirmation.'
        
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            raise ValidationError({
                'confirm_password': "Password and Confirm Password do not match."
            })
        
        return cleaned_data