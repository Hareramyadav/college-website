# Generated by Django 3.0.2 on 2022-05-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0028_menu_menu_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenu',
            name='link_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
