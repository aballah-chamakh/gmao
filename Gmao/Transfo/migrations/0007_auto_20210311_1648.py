# Generated by Django 3.1 on 2021-03-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transfo', '0006_auto_20210311_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfo',
            name='annee_de_creation_primaire',
            field=models.IntegerField(),
        ),
    ]
