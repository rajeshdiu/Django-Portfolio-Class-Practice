# Generated by Django 5.1.1 on 2024-09-21 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_rename_language_name_intermediatelanguagemodel_my_language_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intermediatelanguagemodel',
            old_name='My_Language_Name',
            new_name='Language_Name',
        ),
    ]
