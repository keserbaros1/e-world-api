# Generated by Django 4.2.7 on 2023-12-11 08:22

from django.db import migrations
import django_resized.forms
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_usermodel_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='images/profiles/default.jpg', force_format='JPEG', keep_meta=True, null=True, quality=100, scale=1, size=[500, 500], upload_to=user.models.path_and_rename),
        ),
    ]
