# Generated by Django 5.0.2 on 2024-03-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0010_userquestion_alter_question_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=255)),
                ('user_answer', models.CharField(max_length=255)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
