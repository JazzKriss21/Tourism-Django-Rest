# Generated by Django 3.0.3 on 2020-11-07 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='zip',
            new_name='zipcode',
        ),
    ]
