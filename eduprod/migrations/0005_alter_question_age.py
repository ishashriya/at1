from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('eduprod', '0004_alter_question_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='age',
            field=models.CharField(
                choices=[
                    ('3', '3 years old'),
                    ('4', '4 years old'),
                    ('5', '5 years old'),
                    ('6', '6 years old'),
                    ('7', '7 years old'),
                    ('8', '8 years old')
                ],
                default='3',
                max_length=1  # Adjust the max_length based on your requirement
            ),
        ),
    ]
