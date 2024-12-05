# Generated by Django 5.1.3 on 2024-12-05 09:38

import compressed_image_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_game_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='img',
            field=compressed_image_field.CompressedImageField(default='default_profile.jpg', null=True, quality=80, upload_to='profiles'),
        ),
    ]
