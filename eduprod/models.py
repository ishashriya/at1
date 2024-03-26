from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    topics = [
        ('Addition', '+'),
        ('Subtraction', '-')
    ]


    subject = models.CharField(max_length=200, choices=topics, default='General')
    question_text = models.CharField(max_length=200, default='')
    answer_text = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.question_text