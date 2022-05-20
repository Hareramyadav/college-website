# Generated by Django 3.0.2 on 2022-05-19 19:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0031_auto_20220519_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsection',
            name='about_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsection',
            name='long_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsection',
            name='short_desc',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
