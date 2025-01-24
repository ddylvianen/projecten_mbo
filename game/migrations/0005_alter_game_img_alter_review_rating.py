# Generated by Django 5.1.3 on 2025-01-23 10:08

import compressed_image_field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_game_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='img',
            field=compressed_image_field.CompressedImageField(default='default_profile.jpg', quality=80, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
