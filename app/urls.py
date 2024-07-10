# In myapp/urls.py
from django.urls import path,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
   path('', views.index, name='index'),  # URL pattern for the index page
   path('about/', views.about, name='about'),  # URL pattern for the about page
   path('services/', views.services, name='services'),  # URL pattern for the services page
   path('contact/', views.contact, name='contact'),  # URL pattern for the contact page
   path('registration/', views.registration, name='registration'),  # # URL pattern for the registration page
   path('users/', UserListView.as_view(), name='user-list'),       #URL pattern for the get user details 
   path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'), # URL pattern for get data by mobilenumber
   path('login/', LoginAPIView.as_view(), name='login'),
   path('mentors/', MentorListView.as_view(), name='mentor-list'),
   path('mentors/create/', MentorCreateView.as_view(), name='mentor-create'),
   path('mentors/<int:pk>/', MentorDetailView.as_view(), name='mentor-detail'),
   path('contact-us/', ContactUsCreateView.as_view(), name='contact-us-create'), # URL pattern for the contact us page post api
   path('blog/', include(router.urls)), # this is for blog post
   path('job/', include(router.urls)), # this is for blog post
   

]
