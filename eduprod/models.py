from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import migrations, models


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

    age = models.IntegerField(choices=AGE_CHOICES, default='')  # Default age set to 3 years old
    subject = models.CharField(max_length=200, choices=topics, default='General')
    question_text = models.CharField(max_length=200, default='')
    answer_text = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.question_text
    
    from django.db import migrations, models

def set_default_age(apps, schema_editor):
    Question = apps.get_model('yourappname', 'Question')
    Question.objects.filter(age='').update(age=3)  # Set default value for existing records

class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', 'previous_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='age',
            field=models.IntegerField(choices=[(3, '3 years old'), (4, '4 years old'), (5, '5 years old'), (6, '6 years old'), (7, '7 years old'), (8, '8 years old')], default=3),
            preserve_default=False,  # Remove this line if using a default value
        ),
        migrations.RunPython(set_default_age),
    ]
