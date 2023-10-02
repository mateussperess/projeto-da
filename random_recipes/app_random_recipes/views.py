from django.shortcuts import render
from .models import User

# Create your views here.

def home(request):
  return render(request, 'home.html')

def login(request):
  return render(request, 'users/login.html')

def register(request):
  return render(request, 'users/register.html')


def usuarios(request):
  # Salvando dados da tela no banco de dados
  new_user = User()
  new_user.email = request.POST.get('email')
  new_user.password = request.POST.get('password')
  new_user.save()