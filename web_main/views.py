from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    #return HttpResponse("Hello Zadock")
    return render(request,'templates/homepage.html')

def signup(request):
    return render(request, 'templates/signup.html')
    
def login(request):
    return render(request, 'templates/login.html') 