# Generated by Django 5.1.3 on 2025-01-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_comments_missingreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingreview',
            name='game',
            field=models.CharField(max_length=50),
        ),
    ]
