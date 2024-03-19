from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.TextField()

    def _str_(self):
        return self.question_texts