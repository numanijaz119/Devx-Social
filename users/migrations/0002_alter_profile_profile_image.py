# Generated by Django 5.0.4 on 2024-05-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile-pics/user-default.png', null=True, upload_to='profile-pics/'),
        ),
    ]
