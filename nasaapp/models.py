from distutils.command.upload import upload
import email
from pyexpat import model
from re import T
from statistics import mode
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Menu(models.Model):
    menu_name = models.CharField(max_length=300, null=True, blank=True)
    menu_link = models.CharField(max_length=500, null=True, blank=True)
    menu_position = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return str(self.menu_name)


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    sub_menu_name = models.CharField(max_length=300, null=True, blank=True)
    sub_menu_link = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sub Menu'

    def __str__(self):
        return str(self.sub_menu_name)


class Banner(models.Model):
    banner_image = models.ImageField(
        blank=True, null=True, upload_to="static/banner")
    banner_text = models.CharField(max_length=1000, blank=True, null=True)
    banner_link = models.URLField(max_length=500, null=True, blank=True)
    button_text = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Banner'

    def __str__(self):
        return str(self.banner_text)


class AboutSection(models.Model):
    about_image = models.ImageField(
        blank=True, null=True, upload_to="static/images")
    short_desc = models.TextField(max_length=3000, blank=True, null=True)
    long_desc = models.TextField(max_length=5000, blank=True, null=True)
    about_link = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'About'

    def __str__(self):
        return str(self.about_link)


class News(models.Model):
    news_image = models.ImageField(
        blank=True, null=True, upload_to="static/news")
    title = models.CharField(max_length=1000, blank=True, null=True)
    long_desc = models.TextField(max_length=5000, null=True, blank=True)
    news_link = models.CharField(max_length=300, blank=True, null=True)
    news_position = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'News'

    def __str__(self):
        return str(self.title)


class Message(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    name = models.CharField(max_length=1000, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    long_desc = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Message'

    def __str__(self):
        return str(self.name)


class Gallery(models.Model):
    media = models.FileField(blank=True, null=True, upload_to="static/gallery")
    media_type = models.CharField(max_length=300, null=True, blank=True)
    video_url = models.URLField(max_length=3000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Gallery'

    def __str__(self):
        return str(self.media_type)

class Blog(models.Model):
    blog_image = models.ImageField(blank=True, null=True, upload_to="static/blogs")
    blog_title = models.CharField(max_length=500, blank=True, null=True)
    blog_author = models.CharField(max_length=500, blank=True, null=True)
    short_desc = models.TextField(max_length=1000, blank=True, null=True)
    long_desc = models.TextField(max_length=3000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Blog'

    def __str__(self):
        return str(self.blog_title)

class Testimonial(models.Model):
    student_image = models.ImageField(
        blank=True, null=True, upload_to="static/testimonial")
    student_name = models.CharField(max_length=500, null=True, blank=True)
    short_message = models.TextField(max_length=2000, null=True, blank=True)
    long_message = models.TextField(max_length=5000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Testimonial'

    def __str__(self):
        return str(self.student_name)


class Footer(models.Model):
    heading = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    footer_position = models.CharField(max_length=200, null=True, blank=True)
    quick_links = models.CharField(max_length=3000, null=True, blank=True)
    social_links = models.URLField(max_length=3000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Footer'

    def __str__(self):
        return str(self.footer_position)
