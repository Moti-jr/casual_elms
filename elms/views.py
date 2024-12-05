from django.shortcuts import render

# Create your views here.
def sign_in(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'index.html')


def reset_password(request):
    return render(request, 'reset-password.html')