# Generated by Django 4.2.7 on 2023-12-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_alter_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='faction',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Ferhat Empire'), (2, 'Hilito Empire'), (3, 'Barış Empire'), (4, 'Müno Empire')], null=True),
        ),
    ]