# Generated by Django 4.2.3 on 2023-08-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=30)),
                ('task_description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
