# Generated by Django 4.1 on 2022-08-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leitner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leitner',
            name='d1',
        ),
        migrations.RemoveField(
            model_name='leitner',
            name='d2',
        ),
        migrations.RemoveField(
            model_name='leitner',
            name='d3',
        ),
        migrations.RemoveField(
            model_name='leitner',
            name='m1',
        ),
        migrations.RemoveField(
            model_name='leitner',
            name='m2',
        ),
        migrations.RemoveField(
            model_name='leitner',
            name='w1',
        ),
        migrations.RemoveField(
            model_name='leitner',
            name='w2',
        ),
        migrations.AddField(
            model_name='leitner',
            name='d1',
            field=models.ManyToManyField(blank=True, related_name='d1', to='leitner.lword'),
        ),
        migrations.AddField(
            model_name='leitner',
            name='d2',
            field=models.ManyToManyField(blank=True, related_name='d2', to='leitner.lword'),
        ),
        migrations.AddField(
            model_name='leitner',
            name='d3',
            field=models.ManyToManyField(blank=True, related_name='d3', to='leitner.lword'),
        ),
        migrations.AddField(
            model_name='leitner',
            name='m1',
            field=models.ManyToManyField(blank=True, related_name='m1', to='leitner.lword'),
        ),
        migrations.AddField(
            model_name='leitner',
            name='m2',
            field=models.ManyToManyField(blank=True, related_name='m2', to='leitner.lword'),
        ),
        migrations.AddField(
            model_name='leitner',
            name='w1',
            field=models.ManyToManyField(blank=True, related_name='w1', to='leitner.lword'),
        ),
        migrations.AddField(
            model_name='leitner',
            name='w2',
            field=models.ManyToManyField(blank=True, related_name='w2', to='leitner.lword'),
        ),
    ]
