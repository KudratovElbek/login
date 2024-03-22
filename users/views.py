
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('home')  # Redirect to your desired page
    else:
        form = UserCreationForm()
    return render(request, '/templates/register.html', {'form': form})

# def login_request(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to your desired page
#             else:
#                 # Invalid login credentials
#                 message = "Invalid username or password."
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form, 'message': message})

# def logout_request(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page after logout
