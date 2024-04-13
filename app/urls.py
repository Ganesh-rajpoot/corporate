# In myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),  # URL pattern for the index page
   path('about/', views.about, name='about'),  # URL pattern for the about page
   path('services/', views.services, name='services'),  # URL pattern for the services page
   path('contact/', views.contact, name='contact'),  # URL pattern for the contact page
   path('registration/', views.registration, name='registration'),  # URL pattern for the registration page
]
