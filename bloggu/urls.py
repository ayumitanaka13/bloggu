from django.urls import path
from . import views

app_name = 'bloggu'
urlpatterns = [
    path('', views.home, name='homepage')
]