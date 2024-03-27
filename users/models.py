from django.db import migrations, models

def set_default_age(apps, schema_editor):
    Question = apps.get_model('eduprod', 'Question')
    # Set default age for existing instances
    Question.objects.filter(age='').update(age=3)

class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', 'eduprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='age',
            field=models.CharField(max_length=2, choices=[(3, '3 years old'), (4, '4 years old'), (5, '5 years old'), (6, '6 years old'), (7, '7 years old'), (8, '8 years old')], default=3),
            preserve_default=False,  # Remove this line if using a default value
        ),
        migrations.RunPython(set_default_age),
    ]
