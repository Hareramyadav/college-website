# Generated by Django 3.0.2 on 2022-05-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0018_auto_20220511_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='video_url',
            field=models.URLField(blank=True, max_length=3000, null=True),
        ),
    ]
