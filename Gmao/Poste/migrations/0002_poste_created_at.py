# Generated by Django 3.1 on 2021-03-10 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Poste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
