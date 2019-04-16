from django.shortcuts import render


def index(request):
    return render(request, 'secondWebapp/home.html')


def contact(request):
    return render(request, 'secondWebapp/basic.html')


