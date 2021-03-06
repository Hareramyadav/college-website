from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('create_menu', views.create_menu, name="create_menu"),
    path('edit_menu/<int:menu_id>', views.edit_menu, name="edit_menu"),
    path('delete_menu/<int:menu_id>', views.delete_menu, name="delete_menu"),
    path('create_footer', views.create_footer, name="create_footer"),
    path('edit_footer/<int:footer_id>', views.edit_footer, name="edit_footer"),
    path('delete_footer/<int:footer_id>', views.delete_footer, name="delete_footer"),
    path('about', views.about, name="about"),
    path('news', views.news, name="news"),
    path('gallery', views.gallery, name="gallery"),
    path('blogs', views.blogs, name="blogs"),
    path('blogs/<int:blog_id>', views.blog_single, name="blogs"),
    path('create_banner', views.create_banner, name="create_banner"),
    path('edit_banner/<int:banner_id>', views.edit_banner, name="edit_banner"),
    path('delete_banner/<int:banner_id>', views.delete_banner, name="delete_banner"),
    path('create_about', views.create_about, name="create_about"),
    path('edit_about/<int:about_id>', views.edit_about, name="edit_about"),
    path('delete_about/<int:about_id>', views.delete_about, name="delete_about"),
    path('create_news', views.create_news, name="create_news"),
    path('delete_news/<int:news_id>', views.delete_news, name="delete_news"),
    path('create_gallery', views.create_gallery, name="create_gallery"),
    path('edit_gallery/<int:gallery_id>', views.edit_gallery, name="edit_gallery"),
    path('delete_gallery/<int:gallery_id>', views.delete_gallery, name="delete_gallery"),
    path('create_blog', views.create_blog, name="create_blog"),
    path('edit_blog/<int:blog_id>', views.edit_blog, name="edit_blog"),
    path('delete_blog/<int:blog_id>', views.delete_blog, name="delete_blog"),
    path('create_testimonial', views.create_testimonial, name="create_testimonial"),
    path('edit_testimonial/<int:test_id>', views.edit_testimonial, name="edit_testimonial"),
    path('delete_testimonial/<int:test_id>', views.delete_testimonial, name="delete_testimonial"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('testimonials/<int:test_id>', views.testimonial_single, name="testimonials"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)