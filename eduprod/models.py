from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import migrations, models
from django.core import serializers

class AnswerChoice:
    def __init__(self, answerChoice1, answerChoice2, answerChoice3, answerChoice4):
        self.answerChoice1 = answerChoice1
        self.answerChoice2 = answerChoice2
        self.answerChoice3 = answerChoice3
        self.answerChoice4 = answerChoice4

        @property
        def answerChoice1(self):
            return self.answerChoice1
        
        @answerChoice1.setter
        def answerChoice1(self, value):
            self.answerChoice1 = value

        @property
        def answerChoice2(self):
            return self.answerChoice2
        
        @answerChoice2.setter
        def answerChoice2(self, value):
            self.answerChoice2 = value

        @property
        def answerChoice3(self):
            return self.answerChoice3
        
        @answerChoice3.setter
        def answerChoice3(self, value):
            self.answerChoice3 = value

        @property
        def answerChoice4(self):
            return self.answerChoice4
        
        @answerChoice4.setter
        def answerChoice4(self, value):
            self.answerChoice4 = value
        

class UserQuestion1:
    def __init__(self, id, questionText, answerChoice1, answerChoice2, answerChoice3, answerChoice4, answer):
        self.id = id
        self.questionText = questionText
        self.answerChoice1 = answerChoice1
        self.answerChoice2 = answerChoice2
        self.answerChoice3 = answerChoice3
        self.answerChoice4 = answerChoice4
        self.answer = answer
        
        @property
        def id(self):
            return self.id
        
        @id.setter
        def id(self, value):
            self.id = value

        @property
        def questionText(self):
            return self.questionText
        
        @questionText.setter
        def questionText(self, value):
            self.questionText = value  

        @property
        def answerChoice1(self):
            return self.answerChoice1
        
        @answerChoice1.setter
        def answerChoice1(self, value):
            self.answerChoice1 = value

        @property
        def answerChoice2(self):
            return self.answerChoice2
        
        @answerChoice2.setter
        def answerChoice2(self, value):
            self.answerChoice2 = value

        @property
        def answerChoice3(self):
            return self.answerChoice3
        
        @answerChoice3.setter
        def answerChoice3(self, value):
            self.answerChoice3 = value

        @property
        def answerChoice4(self):
            return self.answerChoice4
        
        @answerChoice4.setter
        def answerChoice4(self, value):
            self.answerChoice4 = value

        @property
        def answer(self):
            return self.answer
        
        @answer.setter
        def answer(self, value):
            self.answer = value

class UserAnswer(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    answer = models.CharField(max_length=255)
    user_answer = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    def serialize(self):
        return {
            'id': self.id,
            'answer': self.answer,
            'user_answer': self.user_answer,
            'score': self.score,
        }
    
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
    

class QuestionManager:
    def __init__(self, topic):
            print(topic)
            self.topic = topic
            self.questions = []  # list of question objects

    def get_questions(self):
        print("Getting questions for " + str(self.topic))
        if self.topic == "EarlyLearning":
            # Implement your logic here using the topic parameter
            #self.questions = [self.createQuestion1(), self.createQuestion2(), self.createQuestion3()]
            print("Returning questions for " + str(self.topic))
            self.questions = EarlyLearningQuestions.get_questions(self)
            return self.questions
        return self.questions
    
class EarlyLearningQuestions:
    def __init__(self):
        self.questions = []  # list of questions from early learning

    def get_questions(self):
        #self.addEarlyLearningQuestion(self.question1())
        #self.addEarlyLearningQuestion(self.question2())
        #self.addEarlyLearningQuestion(self.question3())
        #self.questions = [self.question1(self), self.question2(), self.question3()]
        self.questions = [
            UserQuestion(1, "Question 1 Square", "circle", "triangle", "square", "rectangle", "square"),
            UserQuestion(2, "Question 2 Circle", "circle", "triangle", "square", "rectangle", "circle"),
            UserQuestion(3, "Question 3 Rectangle", "circle", "triangle", "square", "rectangle", "rectangle")
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
