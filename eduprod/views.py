from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


@login_required
def home(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions)
    return render(request, 'eduprod/home.html', {'questions_json': questions_json})

@login_required
def home(request):
    return render(request, 'eduprod/home.html')

@login_required
def get_questions(request):
    age = request.GET.get('age')
    questions = Question.objects.filter(age=age)
    questions_data = serializers.serialize('json', questions)
    return JsonResponse(questions_data, safe=False)
