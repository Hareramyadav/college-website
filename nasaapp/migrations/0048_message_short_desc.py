# Generated by Django 3.0.2 on 2022-06-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0047_auto_20220606_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='short_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
