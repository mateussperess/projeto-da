from django.urls import path
from . import views

app_name = 'app_random_recipes'
urlpatterns = [
  path('login/', views.Login.as_view(), name = 'login'),
  path('register/', views.Register.as_view(), name = "register"),
]