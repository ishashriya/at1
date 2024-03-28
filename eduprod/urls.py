from django.urls import path
from . import views

app_name = 'eduprod'

urlpatterns = [
    path('', views.home, name='home'),
    path('get_questions/', views.get_questions, name='get_questions'),
]
