from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


@login_required(login_url='/accounts/signup')
def home(request):
    return render(request, 'eduprod/home.html')

@login_required(login_url='/accounts/signup')
def get_questions(request):
    topic = request.GET.get('topic')
    questions = Question.objects.filter(topic=topic)  # Assuming 'topic' is a field in your Question model
    data = [{'question_text': question.question_text} for question in questions]
    return JsonResponse(data, safe=False)
