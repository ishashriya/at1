from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_questions/', views.get_questions, name='get_questions'),
]
