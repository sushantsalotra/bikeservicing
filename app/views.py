from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'app/index.html')

def contactus(request):
    return render(request,'app/contactus.html')

def services(request):
    return render(request,'app/services.html')
