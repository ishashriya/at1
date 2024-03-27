from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0002_question_subject_alter_question_answer_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='age',
            field=models.IntegerField(choices=[(3, '3 years old'), (4, '4 years old'), (5, '5 years old'), (6, '6 years old'), (7, '7 years old'), (8, '8 years old')], null=True, blank=True),
        ),
    ]
