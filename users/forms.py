from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(min_length=3, max_length=20,label="Username")
    first_name = forms.CharField(min_length=3,max_length=20,label="Name")
    last_name = forms.CharField(min_length=2, max_length=20, label="Surname")
    email = forms.EmailField(max_length=254)
    password = forms.CharField(min_length=8, max_length=20,label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(min_length=8, max_length=20, label="Confirm Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords don't match!")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    