from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def index_view(request):
    return render(request,'htmlss/index.html')

def about_view(request):
    return render(request,'htmlss/about.html')


def contact_view(request):
    return render(request,'htmlss/contact.html') 
    