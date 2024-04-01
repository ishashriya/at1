from django.shortcuts import render
from .models import Question, QuestionManager, UserAnswer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers

@login_required(login_url='/accounts/signup')
def home(request):
    selected_age = request.GET.get('age')  # Get the selected age from the request
    # questions = Question.objects.all()
    # questions= QuestionManager.questions
    return render(request, 'eduprod/home.html', {'selected_age': selected_age})
    # return render(request, 'eduprod/home.html', {'questions': questions})


@login_required(login_url='/accounts/signup')
def get_questions2(request):
    #topic = request.GET.get('topic')
    # questions = Question.objects.filter(subject=topic)
    # question_data = [{'question_text': question.question_text, 'image_url': question.image.url} for question in questions]
    questions= QuestionManager.questions
    serialized_questions = serializers.serialize('json', questions)
    return JsonResponse(serialized_questions, safe=False)


#class UserQuestion:
#    def __init__(self, id, questionText, answerChoice1, answerChoice2, answerChoice3, answerChoice4, answer):
#        self.id = id
#        self.questionText = questionText
#        self.answerChoice1 = answerChoice1
#       self.answerChoice2 = answerChoice2
#       self.answerChoice3 = answerChoice3
#       self.answerChoice4 = answerChoice4
#       self.answer = answer

def get_questions(request):
    topic = request.GET.get('topic')
    #userID = request.session['user']
    user_answer = UserAnswer().serialize()
    #serialized_user_answer = user_answer.serialize()

    questions = []

    # Assuming you have a list of UserQuestion objects
    # You need to serialize each object into a dictionary
    # and then add it to the questions list
    for user_question in QuestionManager(topic).get_questions():
        question_dict = {
            'id': user_question.id,
            'question_text': user_question.question_text,
            'answer_choice1': user_question.answer_choice1,
            'answer_choice2': user_question.answer_choice2,
            'answer_choice3': user_question.answer_choice3,
            'answer_choice4': user_question.answer_choice4,
            'answer': user_question.answer
        }
        questions.append(question_dict)

    # Finally, return the JsonResponse with the list of questions
    return JsonResponse({'questions': questions, 'user_answer':user_answer}, safe=False)