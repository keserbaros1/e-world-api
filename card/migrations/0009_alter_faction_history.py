# Generated by Django 4.2.7 on 2023-12-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_faction_remove_card_rarity_alter_card_faction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faction',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
    ]
