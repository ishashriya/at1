from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('home3-4', views.home34, name='home3-4'),
    path ('home5-6', views.home56, name='home5-6'),
    path ('home7-8', views.home78, name='home7-8')
]

