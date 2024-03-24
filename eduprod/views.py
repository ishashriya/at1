from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def index(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions)
    return render(request, 'eduprod/index.html', {'questions_json': questions_json})

@login_required
def home34(request):
    return render(request, 'eduprod/home3-4.html')

@login_required
def home56(request):
    return render(request, 'eduprod/home5-6.html')

@login_required
def home78(request):
    return render(request, 'eduprod/home7-8.html')