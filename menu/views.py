from django.shortcuts import render

def home(request):
    return render(request, 'menu/home.html')

def about(request):
    return render(request, 'menu/about.html')

def services(request):
    return render(request, 'menu/services.html')

def contact(request):
    return render(request, 'menu/contact.html')

def consulting(request):
    return render(request, 'menu/consulting.html')

def development(request):
    return render(request, 'menu/development.html')
