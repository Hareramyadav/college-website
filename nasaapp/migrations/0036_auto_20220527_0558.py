# Generated by Django 3.0.2 on 2022-05-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0035_footer_license_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='tiktok',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='facebook',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='instagram',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='twitter',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='youtube',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
