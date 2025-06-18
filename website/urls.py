from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('courses/', views.courses_view, name='courses'),
    path('contact/', views.contact_view, name='contact'),
    #path('feedback/', views.feedback_view, name='feedback'),
    path('login/', views.login_view, name='login'),
    
    
]
