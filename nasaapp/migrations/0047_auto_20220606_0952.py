# Generated by Django 3.0.2 on 2022-06-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0046_auto_20220531_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]