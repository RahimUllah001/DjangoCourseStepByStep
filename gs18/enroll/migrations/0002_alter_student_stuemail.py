# Generated by Django 5.1 on 2024-09-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stuemail',
            field=models.EmailField(max_length=60),
        ),
    ]
