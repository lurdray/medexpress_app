# Generated by Django 3.1.7 on 2022-01-10 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_auto_20220110_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pramdata',
            old_name='Intrauterine',
            new_name='intrauterine',
        ),
    ]