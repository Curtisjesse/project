
from django.urls import path 
from . import views

app_name = 'web'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.departments, name='departments'),
    path('doctor/', views.doctor, name='doctor'),
    path('appointment/', views.appointment, name='appointment'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]