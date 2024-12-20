# blog/forms.py
from django import forms
from .models import CustomUser

# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_image']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data


# User Profile Update Form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_image']


# Contact Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        error_messages={
            'invalid': "Enter a valid phone number."
        },
        label="Phone Number",
    )
    attachment = forms.FileField(required=False, label="Attach a File")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
