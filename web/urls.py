
from django.urls import path 
from . import views

app_name = 'web'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact_info/', views.contact_info, name='contact_info'),
    path('departments/', views.departments, name='departments'),
    path('doctor/', views.doctor, name='doctor'),
    path('appointment/', views.appointment, name='appointment'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('login/', views.login, name='login'),
    path('medicine/', views.medicine, name='medicine'),
    #path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('booking/<str:doctor_id>/', views.book_doctor, name='booking'),
    
    
]