# Generated by Django 3.1 on 2021-03-21 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AffiliateCompany', '0002_auto_20210321_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiliatecompany',
            name='address',
        ),
        migrations.RemoveField(
            model_name='affiliatecompany',
            name='city',
        ),
        migrations.RemoveField(
            model_name='affiliatecompany',
            name='country',
        ),
        migrations.RemoveField(
            model_name='affiliatecompany',
            name='email',
        ),
        migrations.RemoveField(
            model_name='affiliatecompany',
            name='tel',
        ),
    ]