# Generated by Django 3.1.4 on 2021-09-21 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210921_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='vote_ration',
            new_name='vote_ratio',
        ),
    ]
