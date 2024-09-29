from django.contrib import admin
from django.urls import path
from menu import views  # Импортируем views из приложения menu

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('services/development', views.development, name='development'),
    path('services/consulting', views.consulting, name='consulting')
]
