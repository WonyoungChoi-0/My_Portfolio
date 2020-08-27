from django.urls import path
from portfolio import views
app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('industry/', views.industry, name="industry"),
    path('resume/', views.resume, name="resume"),
]
