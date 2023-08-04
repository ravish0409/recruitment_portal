 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job_search/', views.job_search, name='job_search'),
    path('candidate_profile/', views.candidate_profile, name='candidate_profile'),
]
