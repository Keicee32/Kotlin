# Generated by Django 3.0.7 on 2020-06-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anchor', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
        ),
    ]
