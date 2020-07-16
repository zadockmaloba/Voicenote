from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('home/', views.homepage, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login')
]