# Generated by Django 2.2.5 on 2020-02-09 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200120_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='guset',
            new_name='guest',
        ),
    ]