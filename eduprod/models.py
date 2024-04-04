from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import migrations, models
from django.core import serializers


# Model representing the UserAnswer
class UserAnswer(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    answer = models.CharField(max_length=255)
    user_answer = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    # Serialize method to convert to dictionary
    def serialize(self):
        return {
            'id': self.id,
            'answer': self.answer,
            'user_answer': self.user_answer,
            'score': self.score,
        }
    
# Model representing the UserQuestion
class UserQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=255)
    answer_choice1 = models.CharField(max_length=255)
    answer_choice2 = models.CharField(max_length=255)
    answer_choice3 = models.CharField(max_length=255)
    answer_choice4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
    
# Class representing the QuestionManager
class QuestionManager:
    def __init__(self, topic):
            print(topic)
            self.topic = topic
            self.questions = []  # list of question objects

    # Method to get questions
    def get_questions(self):
        print("Getting questions for " + str(self.topic))
        if self.topic == "EarlyLearning":
            # Implement your logic here using the topic parameter
            #self.questions = [self.createQuestion1(), self.createQuestion2(), self.createQuestion3()]
            print("Returning questions for " + str(self.topic))
            self.questions = EarlyLearningQuestions.get_questions(self)
            return self.questions
        return self.questions
    
    # Class representing the EarlyLearningQuestions
class EarlyLearningQuestions:
    def __init__(self):
        self.questions = []  # list of questions from early learning

    # Method to get early learning questions
    def get_questions(self):
        self.questions = [
            UserQuestion(1, "square", "circle", "triangle", "square", "rectangle", "square"),
            UserQuestion(2, "circle", "circle", "triangle", "square", "rectangle", "circle"),
            UserQuestion(3, "rectangle", "circle", "triangle", "square", "rectangle", "rectangle"),
            UserQuestion(4, "oval", "circle", "triangle", "square", "oval", "oval"),
            UserQuestion(5, "trapezoid", "trapezoid", "rectangle", "square", "oval", "trapezoid"),
            UserQuestion(6, "parallelogram", "rectangle", "parallelogram", "square", "oval", "parallelogram"),
            UserQuestion(7, "triangle", "circle", "triangle", "square", "oval", "triangle")
        ]
        return self.questions

    def addEarlyLearningQuestion(self, question):
        self.questions.append(question)

    def question1(self):
        q1 = UserQuestion(1, "Question 1 Square", "circle", "triangle", "square", "rectangle", "square") # Create a question with 5 choices
        return q1
    
    def question2(self):
        q2 = UserQuestion(2, "Question 2 Circle", "circle", "triangle", "square", "rectangle", "circle") # Create a question with 5 choices
        return q2

    def question3(self):
        q3 = UserQuestion(3, "Question 3 Rectangle", "circle", "triangle", "square", "rectangle", "rectangle") # Create a question with 5 choices
        return q3


    
      

class AnswerManager:
    def __init__(self):
        self._answers = {}
        
    user_answer = UserAnswer()

#         @property
#         def is_answered(self):
#             return bool(self.answer)
            
#     answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    
# class QuestionManager(models.Manager):
#     def add_question(self, text, author):
#         q = self.model()
#         q.text = text
#         q.author = author
#         q.save()
#         return q

# class AnswerManager(models.Manager):
#     def add_answer(self, text, question, author):
#         a = super().create(text=text, question=question, author=author)
#         question.answer = a
#         question.save()
#         return a
    
# Model representing the Question
class Question(models.Model):
    topics = [
        ('Shapes', '#'),
        ('Addition', '+'),
        ('Subtraction', '-'),
        ('Multiplication', '*'),
        ('Divison', '/')
    ]

    AGE_CHOICES = [
        ('3', '3 years old'),
        ('4', '4 years old'),
        ('5', '5 years old'),
        ('6', '6 years old'),
        ('7', '7 years old'),
        ('8', '8 years old')
    ]

    age = models.CharField(max_length=1, choices=AGE_CHOICES, default='3')
    subject = models.CharField(max_length=200, choices=topics, default='General')
    question_text = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='question_images/', default='')  # New field for the image
    correct_answer = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.question_text

def set_default_age(apps, schema_editor):
    Question = apps.get_model('eduprod', 'Question')
    Question.objects.filter(age='').update(age=3)  # Set default value for existing records

class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', 'eduprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='age',
            field=models.CharField(choices=[(3, '3 years old'), (4, '4 years old'), (5, '5 years old'), (6, '6 years old'), (7, '7 years old'), (8, '8 years old')], default=3),
            preserve_default=False,  # Remove this line if using a default value
        ),
        migrations.RunPython(set_default_age),
    ]
