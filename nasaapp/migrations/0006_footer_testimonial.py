# Generated by Django 3.0.2 on 2022-05-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasaapp', '0005_gallery_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=1000, null=True)),
                ('content', models.CharField(blank=True, max_length=3000, null=True)),
                ('footer_position', models.CharField(blank=True, max_length=200, null=True)),
                ('links', models.CharField(blank=True, max_length=3000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_image', models.ImageField(blank=True, null=True, upload_to='static/testimonial')),
                ('student_name', models.CharField(blank=True, max_length=500, null=True)),
                ('message', models.TextField(blank=True, max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Testimonial',
            },
        ),
    ]
