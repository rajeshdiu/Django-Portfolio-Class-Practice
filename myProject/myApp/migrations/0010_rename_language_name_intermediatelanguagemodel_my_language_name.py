# Generated by Django 5.1.1 on 2024-09-21 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_alter_languagemodel_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intermediatelanguagemodel',
            old_name='Language_Name',
            new_name='My_Language_Name',
        ),
    ]
