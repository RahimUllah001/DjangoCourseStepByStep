# Generated by Django 5.1 on 2024-10-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('school.examcenter',),
        ),
    ]
