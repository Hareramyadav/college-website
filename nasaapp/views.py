from datetime import date
from email.policy import HTTP
import os
import site
from tkinter.messagebox import NO
from turtle import heading, tilt, update
from xxlimited import foo
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
import math
from math import ceil

# Create your views here.


def index(request):
    banner = Banner.objects.all().order_by('created_at')
    about = AboutSection.objects.all().order_by('created_at')[:1]
    news = News.objects.all().order_by('created_at')
    messages = Message.objects.all().order_by('created_at')[:4]
    main_news = [m for m in news if m.news_position == 'main_news'][:1]
    side_news = [s for s in news if s.news_position == 'side_news'][:3]
    blogs = Blog.objects.all().order_by('created_at')[:2]
    gallery = Gallery.objects.all().order_by('created_at')
    image = [i for i in gallery if i.media_type == 'image']
    video = [v for v in gallery if v.media_type == 'video']
    testimonial = Testimonial.objects.all()[:6]
    testimonial_no = len(testimonial)
    testimonial_slide = testimonial_no // 3 + \
        ceil((testimonial_no / 3) - (testimonial_no // 3))
    header_footer = header_footer_view(request)
    data = {
        'banner': banner,
        'about': about,
        'main_news': main_news,
        'side_news': side_news,
        'messages': messages,
        'blog': blogs,
        'image': image,
        'video': video,
        'testimonial': testimonial,
        'testimonial_slide': testimonial_slide,
        'range': range(testimonial_slide),
    }
    data.update(header_footer)
    return render(request, 'index.html', data)


def header_footer_view(request):
    menu_lists = Menu.objects.all().order_by('created_at')
    sub_menu_lists = SubMenu.objects.all()
    top_header = [m for m in menu_lists if m.menu_position == 'topheader']
    bottom_header = [
        m for m in menu_lists if m.menu_position == 'bottomheader']
    footer = Footer.objects.all().order_by('created_at')
    footer_first = [
        f for f in footer if f.footer_position == 'footer_first'][:1]
    print('footer first', footer_first)
    footer_second = [
        s for s in footer if s.footer_position == 'footer_second'][:1]
    footer_third = [
        t for t in footer if t.footer_position == 'footer_third'][:1]
    return ({
        'top_header': top_header,
        'bottom_header': bottom_header,
        'sub_menu': sub_menu_lists,
        'footer_first': footer_first,
        'footer_second': footer_second,
        'footer_third': footer_third
    })


def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')


def site_identity(request):
    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        tagline = request.POST.get('tagline')
        logo_first = request.FILES.get('logo_first')
        logo_second = request.FILES.get('logo_second')
        favicon = request.FILES.get('favicon')

        data = dict(site_name=site_name, tagline=tagline,
                    logo_first=logo_first, logo_second=logo_second, favicon=favicon)

        if(SiteIdentity.objects.all().count() >= 1):
            messages.warning(
                request, 'Cannot create more than one site identity.')
            return redirect('/site_identity')
        SiteIdentity.objects.create(**data)
        return redirect('/site_identity')
    site_identity = SiteIdentity.objects.all().order_by('created_at')
    return render(request, 'admin/site_identity.html', {'site_identity': site_identity})


def edit_identity(request, site_id):
    site_identity = SiteIdentity.objects.get(id=int(site_id))
    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        tagline = request.POST.get('tagline')
        logo_first = request.FILES.get('logo_first', None)
        logo_second = request.FILES.get('logo_second', None)
        favicon = request.FILES.get('favicon', None)

        site_identity.site_name = site_name
        site_identity.tagline = tagline
        if logo_first is not None:
            site_identity.logo_first = logo_first
        if logo_second is not None:
            site_identity.logo_second = logo_second
        if favicon is not None:
            site_identity.favicon = favicon
        site_identity.save()
        return redirect('/site_identity')
    return render(request, 'admin/edit_identity.html', {'site_identity': site_identity, 'site_id': site_id})


def create_footer(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        footer_position = request.POST.get('footer_position')
        quick_links = request.POST.get('quick_links')
        social_links = request.POST.get('social_links')

        data = dict(heading=heading, address=address, phone_number=phone_number, email=email,
                    footer_position=footer_position, quick_links=quick_links, social_links=social_links)
        if(Footer.objects.all().count() >= 3):
            messages.warning(request, "You can create only 3 footers")
            return HttpResponseRedirect('/create_footer')
        Footer.objects.create(**data)
        return HttpResponseRedirect('/create_footer')
    header_footer = header_footer_view(request)
    footer = Footer.objects.all().order_by('created_at')
    data = {'footer': footer}
    data.update(header_footer)
    return render(request, 'admin/create_footer.html', data)


def edit_footer(request, footer_id):
    footer = Footer.objects.get(id=int(footer_id))
    if request.method == 'POST':
        heading = request.POST.get('heading')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        footer_position = request.POST.get('footer_position')
        quick_links = request.POST.get('quick_links')
        social_links = request.POST.get('social_links')

        footer.heading = heading
        footer.address = address
        footer.phone_number = phone_number
        footer.email = email
        footer.footer_position = footer_position
        footer.quick_links = quick_links
        footer.social_links = social_links

        footer.save()
        return redirect('/create_footer')
    header_footer = header_footer_view(request)
    data = {'footer': footer, 'footer_id': footer_id}
    data.update(header_footer)
    return render(request, 'admin/edit_footer.html', data)


def delete_footer(request, footer_id):
    Footer.objects.filter(id=int(footer_id)).delete()
    return redirect('/create_footer')


def create_menu(request):
    if request.method == 'POST':
        menu_name = request.POST.get('menu_name')
        menu_link = request.POST.get('menu_link')
        menu_position = request.POST.getlist('menu_position')[0]

        data = dict(menu_name=menu_name, menu_link=menu_link,
                    menu_position=menu_position)
        Menu.objects.create(**data)
        return HttpResponseRedirect('/create_menu')
    header_footer = header_footer_view(request)
    menu = Menu.objects.all().order_by('created_at')
    data = {'menu': menu}
    data.update(header_footer)
    return render(request, 'admin/create_menu.html', data)


def edit_menu(request, menu_id):
    menu = Menu.objects.get(id=int(menu_id))
    if request.method == 'POST':
        menu_name = request.POST.get('menu_name')
        menu_link = request.POST.get('menu_link')
        menu_position = request.POST.getlist('menu_position')

        menu.menu_name = menu_name
        menu.menu_link = menu_link

        menu.save()
        return redirect('/create_menu')
    return render(request, 'admin/edit_menu.html', {'menu': menu, 'menu_id': menu_id})


def delete_menu(request, menu_id):
    Menu.objects.filter(id=int(menu_id)).delete()
    return redirect('/create_menu')


def create_banner(request):
    if request.method == 'POST':
        banner_image = request.FILES.get('banner_image')
        banner_text = request.POST.get('banner_text')
        banner_link = request.POST.get('banner_link')
        button_text = request.POST.get('button_text')
        data = dict(banner_image=banner_image, banner_text=banner_text,
                    banner_link=banner_link, button_text=button_text)
        Banner.objects.create(**data)
        return HttpResponseRedirect('/create_banner')
    banner = Banner.objects.all().order_by('created_at')
    return render(request, 'admin/create_banner.html', {'banner': banner})


def edit_banner(request, banner_id):
    banner = Banner.objects.get(id=int(banner_id))
    if request.method == 'POST':
        banner_image = request.FILES.get('banner_image', None)
        banner_text = request.POST.get('banner_text')
        banner_link = request.POST.get('banner_link')
        button_text = request.POST.get('button_text')

        banner.banner_text = banner_text
        banner.banner_link = banner_link
        banner.button_text = button_text
        if banner_image is not None:
            banner.banner_image = banner_image
        banner.save()
        return redirect('/create_banner')
    data = {'banner': banner, 'banner_id': banner_id}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'admin/edit_banner.html', data)


def delete_banner(request, banner_id):
    Banner.objects.filter(id=int(banner_id)).delete()
    return HttpResponseRedirect('/create_banner')


def create_about(request):
    if request.method == 'POST':
        about_image = request.FILES.get('about_image')
        short_desc = request.POST.get('short_desc')
        long_desc = request.POST.get('long_desc')
        about_link = request.POST.get('about_link')
        data = dict(about_image=about_image, short_desc=short_desc,
                    long_desc=long_desc, about_link=about_link)
        AboutSection.objects.create(**data)
        return redirect('/create_about')
    about = AboutSection.objects.all().order_by('created_at')
    return render(request, 'admin/create_about.html', {'about': about})


def edit_about(request, about_id):
    about = AboutSection.objects.get(id=int(about_id))
    if request.method == 'POST':
        about_image = request.FILES.get('about_image', None)
        short_desc = request.POST.get('short_desc')
        long_desc = request.POST.get('long_desc')
        about_link = request.POST.get('about_link')

        about.short_desc = short_desc
        about.long_desc = long_desc
        about.about_link = about_link
        if about_image is not None:
            about.about_image = about_image
        about.save()
        return redirect('/create_about')
    return render(request, 'admin/edit_about.html', {'about': about, 'about_id': about_id})


def delete_about(request, about_id):
    AboutSection.objects.filter(id=int(about_id))
    return redirect('/create_about')


def create_news(request):
    if request.method == 'POST':
        news_image = request.FILES.get('news_image')
        title = request.POST.get('title')
        long_desc = request.POST.get('long_desc')
        news_position = request.POST.get('news_position')

        data = dict(news_image=news_image, title=title,
                    long_desc=long_desc, news_position=news_position)
        News.objects.create(**data)
        return redirect('/create_news')
    news = News.objects.all().order_by('created_at')
    return render(request, 'admin/create_news.html', {'news': news})


def delete_news(request, news_id):
    News.objects.filter(id=int(news_id)).delete()
    return redirect('/create_news')


def create_gallery(request):
    if request.method == 'POST':
        media = request.FILES.get('media')
        media_type = request.POST.get('media_type')
        video_url = request.POST.get('video_url')
        data = dict(media=media, media_type=media_type, video_url=video_url)
        Gallery.objects.create(**data)
        return redirect('/create_gallery')
    gallery = Gallery.objects.all().order_by('created_at')
    return render(request, 'admin/create_gallery.html', {'gallery': gallery})


def edit_gallery(request, gallery_id):
    gallery = Gallery.objects.get(id=int(gallery_id))
    if request.method == 'POST':
        media = request.FILES.get('media', None)
        video_url = request.POST.get('video_url')

        gallery.video_url = video_url
        if media is not None:
            gallery.media = media
        gallery.save()
        return redirect('/edit_gallery')
    return render(request, 'admin/edit_gallery.html', {'gallery': gallery, 'gallery_id': gallery_id})


def delete_gallery(request, gallery_id):
    Gallery.objects.filter(id=int(gallery_id)).delete()
    return redirect('/create_gallery')


def create_blog(request):
    if request.method == 'POST':
        blog_image = request.FILES.get('blog_image')
        blog_title = request.POST.get('blog_title')
        blog_author = request.POST.get('blog_author')
        short_desc = request.POST.get('short_desc')
        long_desc = request.POST.get('long_desc')

        data = dict(blog_image=blog_image, blog_title=blog_title,
                    blog_author=blog_author, short_desc=short_desc, long_desc=long_desc)
        Blog.objects.create(**data)
        return redirect('/create_blog')
    blog = Blog.objects.all().order_by('created_at')
    return render(request, 'admin/create_blog.html', {'blog': blog})


def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=int(blog_id))
    if request.method == 'POST':
        blog_image = request.FILES.get('blog_image', None)
        blog_title = request.POST.get('blog_title')
        blog_author = request.POST.get('blog_author')
        short_desc = request.POST.get('short_desc')
        long_desc = request.POST.get('long_desc')

        blog.blog_title = blog_title
        blog.blog_author = blog_author
        blog.short_desc = short_desc
        blog.long_desc = long_desc
        if blog_image is not None:
            blog.blog_image = blog_image
        blog.save()
        return redirect('/create_blog')
    return render(request, 'admin/edit_blog.html', {'blog': blog, 'blog_id': blog_id})


def delete_blog(request, blog_id):
    Blog.objects.filter(id=int(blog_id)).delete()
    return redirect('/create_blog')


def create_testimonial(request):
    if request.method == 'POST':
        student_image = request.FILES.get('student_image')
        student_name = request.POST.get('student_name')
        short_message = request.POST.get('short_message')
        long_message = request.POST.get('long_message')

        data = dict(student_image=student_image, student_name=student_name,
                    short_message=short_message, long_message=long_message)
        testimonial = Testimonial.objects.create(**data)
        return redirect('/create_testimonial')
    testimonial = Testimonial.objects.all().order_by('created_at')
    return render(request, 'admin/create_testimonial.html', {'testimonial': testimonial})


def edit_testimonial(request, test_id):
    testimonial = Testimonial.objects.get(id=int(test_id))
    if request.method == 'POST':
        student_image = request.FILES.get('student_image', None)
        student_name = request.POST.get('student_name')
        short_message = request.POST.get('short_message')
        long_message = request.POST.get('long_message')

        testimonial.student_name = student_name
        testimonial.short_message = short_message
        testimonial.long_message = long_message

        if student_image is not None:
            testimonial.student_image = student_image

        testimonial.save()
        return redirect('/create_testimonial')
    return render(request, 'admin/edit_testimonial.html', {'testimonial': testimonial, 'test_id': test_id})


def delete_testimonial(request, test_id):
    Testimonial.objects.filter(id=int(test_id)).delete()
    return redirect('/create_testimonial')


def create_popup(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        message = request.POST.get('message')

        data = dict(title=title, file=file, message=message)
        Popup.objects.create(**data)
        return redirect('/create_popup')
    popup = Popup.objects.all().order_by('created_at')
    return render(request, 'admin/create_popup.html', {'popup': popup})


def edit_popup(request, popup_id):
    popup = Popup.objects.get(id=int(popup_id))
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file', None)
        message = request.POST.get('message')

        popup.title = title
        popup.message = message
        if file is not None:
            popup.file = file

        popup.save()
        return redirect('/create_popup')
    return render(request, 'admin/edit_popup.html', {'popup': popup, 'popup_id': popup_id})


def delete_popup(request, popup_id):
    Popup.objects.filter(id=int(popup_id)).delete()
    return redirect('/create_popup')

def inquiry_forms(request):
    inquiry_form = AdmissionForm.objects.all().order_by('created_at')
    return render(request, 'admin/inquiry_form.html', {'inquiry_form':inquiry_form})

def delete_form(request, form_id):
    AdmissionForm.objects.filter(id=int(form_id)).delete()
    return redirect('/inquiry_form')

# client pages

def sidebar(request):
    news = News.objects.all().order_by('created_at')[:2]
    return({
        'news': news
    })


def news(request):
    news = News.objects.all().order_by('created_at')
    data = {'news': news}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/news.html', data)


def news_single(request, news_id):
    news = News.objects.get(id=int(news_id))
    data = {'news': news}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/news_single.html', data)


def blogs(request):
    blogs = Blog.objects.all().order_by('created_at')
    data = {'blogs': blogs}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/blogs.html', data)


def blog_single(request, blog_id):
    blog = Blog.objects.get(id=int(blog_id))
    data = {'blog': blog}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/blog_single.html', data)


def gallery(request):
    gallery = Gallery.objects.all().order_by('created_at')
    image = [i for i in gallery if i.media_type == 'image']
    video = [v for v in gallery if v.media_type == 'video']
    data = {'image': image, 'video': video}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/gallery.html', data)


def testimonials(request):
    testimonial = Testimonial.objects.all().order_by('created_at')
    data = {'testimonials': testimonial}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/testimonials.html', data)


def testimonial_single(request, test_id):
    testimonial = Testimonial.objects.get(id=int(test_id))
    data = {'testimonial': testimonial}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/testimonial_single.html', data)


def about(request):
    about = AboutSection.objects.all().order_by('created_at')
    data = {'about': about}
    header_footer = header_footer_view(request)
    sidebars = sidebar(request)
    data.update(header_footer)
    data.update(sidebars)
    return render(request, 'client/about.html', data)


def contact(request):
    footer = Footer.objects.all().order_by('created_at')
    footer_first = [
        f for f in footer if f.footer_position == 'footer_first'][:1]
    footer_third = [
        t for t in footer if t.footer_position == 'footer_third'][:1]
    data = {'footer': footer, 'footer_first': footer_first,
            'footer_third': footer_third}
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/contact.html', data)


def admission_from(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        mobile_no = request.POST.get('mobile_no')
        current_address = request.POST.get('current_address')
        parent_name = request.POST.get('parent_name')
        parent_no = request.POST.get('parent_no')
        parent_email = request.POST.get('parent_email')
        gpa = request.POST.get('gpa')
        school_name = request.POST.get('school_name')
        school_address = request.POST.get('school_address')
        stream = request.POST.get('stream')

        data = dict(
            full_name=full_name,
            email=email,
            date_of_birth=date_of_birth,
            gender=gender,
            mobile_no=mobile_no,
            current_address=current_address,
            parent_name=parent_name,
            parent_no=parent_no,
            parent_email=parent_email,
            gpa=gpa,
            school_name=school_name,
            school_address=school_address,
            stream=stream,
        )
        AdmissionForm.objects.create(**data)
        return redirect('/')
    header_footer = header_footer_view(request)
    return render(request, 'client/admission_from.html', header_footer)