# Generated by Django 3.1.7 on 2021-12-27 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.FileField(blank=True, default='default_files/default_face.png', upload_to='account_files/profile_photos/')),
                ('name', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('address', models.TextField(default='')),
                ('pregancy_status', models.CharField(default='', max_length=20)),
                ('blood_group', models.CharField(default='', max_length=20)),
                ('hiv_status', models.CharField(default='', max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
