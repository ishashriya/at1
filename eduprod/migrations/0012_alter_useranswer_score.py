# Generated by Django 5.0.2 on 2024-03-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0011_useranswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
