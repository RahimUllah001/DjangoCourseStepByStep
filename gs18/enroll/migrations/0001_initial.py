# Generated by Django 5.1 on 2024-09-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuid', models.IntegerField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.CharField(max_length=60)),
                ('stupass', models.CharField(max_length=60)),
            ],
        ),
    ]