# Generated by Django 3.0.2 on 2022-05-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0030_menu_menu_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsection',
            name='about_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
