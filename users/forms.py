# from django import forms
# from django.contrib.auth.models import User

# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Confirm Password (required)", widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email']  # Adjust fields as needed

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password']

# class LoginForm(forms.Form):
#     username = forms.CharField(label="Username")
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
