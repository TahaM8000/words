# Generated by Django 4.1 on 2022-08-22 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_word_learn'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='')),
                ('words', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='words.word')),
            ],
        ),
    ]
