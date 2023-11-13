from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework.views import APIView

# Create your views here.

def home(request):
  return render(request, 'home.html')

class Login(APIView):
    def get(self, request, format=None):
        return render(request, 'users/login.html')

    def post(self, request, format=None):
      return HttpResponse(request.POST.get('email'))
    
    # def register(request):
    #   return render(request, 'users/register.html')
class Register(APIView):
   def get(self, request, format=None):
      return render(request, 'users/register.html')
   
   def post(self, request, format=None):
      return HttpResponse(request.POST.get('email'))
