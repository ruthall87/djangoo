# Generated by Django 3.1.4 on 2020-12-26 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20201226_0507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titleman',
            new_name='title',
        ),
    ]
