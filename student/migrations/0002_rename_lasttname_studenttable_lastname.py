# Generated by Django 3.2.4 on 2021-06-15 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenttable',
            old_name='lasttname',
            new_name='lastname',
        ),
    ]
