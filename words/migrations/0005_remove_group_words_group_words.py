# Generated by Django 4.1 on 2022-08-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='words',
        ),
        migrations.AddField(
            model_name='group',
            name='words',
            field=models.ManyToManyField(to='words.word'),
        ),
    ]
