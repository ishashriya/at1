from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    topics = [
        ('Addition', '+'),
        ('Subtraction', '-')
    ]
    AGE_CHOICES = [
        (3, '3 years old'),
        (4, '4 years old'),
        (5, '5 years old'),
        (6, '6 years old'),
        (7, '7 years old'),
        (8, '8 years old')
    ]

    age = models.IntegerField(choices=AGE_CHOICES, default='General')  # Default age set to 3 years old
    subject = models.CharField(max_length=200, choices=topics, default='General')
    question_text = models.CharField(max_length=200, default='')
    answer_text = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.question_text
