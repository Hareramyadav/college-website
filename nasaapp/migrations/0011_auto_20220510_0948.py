# Generated by Django 3.0.2 on 2022-05-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0010_auto_20220510_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='sub_menu_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
