# Generated by Django 4.1 on 2022-09-01 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leitner', '0005_lword_leitner'),
        ('accounts', '0003_alter_user_leitner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='leitner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='leitner.leitner'),
        ),
    ]
