from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')
def about(request):
    return render(request, 'app/about.html')
def services(request):
    return render(request, 'app/services.html')
def contact(request):
    return render(request, 'app/contact.html')

def registration(request):
    return render(request, 'app/registration.html')