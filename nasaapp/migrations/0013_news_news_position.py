# Generated by Django 3.0.2 on 2022-05-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0012_auto_20220510_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
