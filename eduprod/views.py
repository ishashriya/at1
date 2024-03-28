from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url='/accounts/signup')
def home(request):
    selected_age = request.GET.get('age')  # Get the selected age from the request
    return render(request, 'eduprod/home.html', {'selected_age': selected_age})

@login_required(login_url='/accounts/signup')
def get_questions(request):
    topic = request.GET.get('topic')
    questions = Question.objects.filter(subject=topic)
    data = [{'question_text': question.question_text} for question in questions]
    return JsonResponse(data, safe=False)
