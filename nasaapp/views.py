from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from rest_framework.status import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
import math
from math import ceil
from .verify_request import *
from django.contrib.auth import authenticate, logout
from .forms import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        admin_user = User.objects.filter(email=email)
        admin_username = admin_user[0].username if len(admin_user ) > 0 else None
        print('username', admin_username)
        is_admin = authenticate(username=admin_username, password=password)

        if is_admin is None:
            error = "User email or password does not match"
            messages.info(request, error)
            return HttpResponseRedirect('/admin_login')
        else:
            request.session['user'] = email
            request.session['islogin'] = True
            return redirect('/admin_dashboard')
    return render(request, 'admin/login.html')
    
def admin_logout(request):
    logout(request)
    return redirect('/admin_login')

def index(request):
    banner = Banner.objects.all().order_by('created_at')
    menu = Menu.objects.all()
    popup = Popup.objects.all()
    about = AboutSection.objects.all().order_by('created_at')[:1]
    news = News.objects.all().order_by('created_at')
    main_news = News.objects.all().order_by('-created_at')[0:1]
    side_news = News.objects.all().order_by('-created_at')[1:3]
    messages = Message.objects.all().order_by('created_at')[:4]
    blogs = Blog.objects.all().order_by('created_at')[:2]
    gallery = Gallery.objects.all().order_by('created_at')
    image = [i for i in gallery if i.media_type == 'image']
    video = [v for v in gallery if v.media_type == 'video']
    testimonial = Testimonial.objects.all()[:6]
    testimonial_no = len(testimonial)
    testimonial_slide = testimonial_no // 3 + \
        ceil((testimonial_no / 3) - (testimonial_no // 3))
    testimonial_mobile_silde = testimonial_no // 1 + \
        ceil((testimonial_no / 1) - (testimonial_no // 1))
    header_footer = header_footer_view(request)
    data = {
        'banner': banner,
        'menu':menu,
        'popup':popup,
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
        'testimonial_mobile_silde':testimonial_mobile_silde,
        'range_mobile':range(testimonial_mobile_silde),
    }
    data.update(header_footer)
    return render(request, 'index.html', data)


def menu_info_content(request, menu_id):
    menu = Menu.objects.get(id=int(menu_id))
    data = {
        'menu_data':menu
    }
    header_footer = header_footer_view(request)
    sidebars = sidebar(request)
    data.update(header_footer)
    data.update(sidebars)
    return render(request, 'client/info.html', data)

def header_footer_view(request):
    site_identity = SiteIdentity.objects.all().order_by('created_at')
    menu_lists = Menu.objects.all().order_by('-created_at')
    dropdown_menu = [d for d in menu_lists if d.menu_type == 'dropdown']
    link_menu = [l for l in menu_lists if l.menu_type == 'link']
    sub_menu_lists = SubMenu.objects.all()
    top_header = [m for m in menu_lists if m.menu_position == 'topheader']
    bottom_header = [
        m for m in menu_lists if m.menu_position == 'bottomheader']
    footer = Footer.objects.all().order_by('created_at')[:1]
    return ({
        'top_header': top_header,
        'bottom_header': bottom_header,
        'menu_list':menu_lists,
        'dropdown_menu':dropdown_menu,
        'link_menu':link_menu,
        'sub_menu': sub_menu_lists,
        'footer':footer,
        'site_identity':site_identity,
    })

@validate_request_for_admin
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

@validate_request_for_admin
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

@validate_request_for_admin
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

@validate_request_for_admin
def create_footer(request):
    form = FooterForm()
    if request.method == 'POST':
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        youtube = request.POST.get('youtube')
        copyright = request.POST.get('copyright')

        data = dict(address=address, phone_number=phone_number, email=email, 
            facebook=facebook, instagram=instagram, twitter=twitter, youtube=youtube, copyright=copyright)
        if(Footer.objects.all().count() >= 3):
            messages.warning(request, "You can create only 3 footers")
            return HttpResponseRedirect('/create_footer')
        Footer.objects.create(**data)
        return HttpResponseRedirect('/create_footer')
    header_footer = header_footer_view(request)
    footer = Footer.objects.all().order_by('created_at')
    data = {'footer': footer, 'form':form}
    data.update(header_footer)
    return render(request, 'admin/create_footer.html', data)

@validate_request_for_admin
def edit_footer(request, footer_id):
    form = FooterForm()
    footer = Footer.objects.get(id=int(footer_id))
    if request.method == 'POST':
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        youtube = request.POST.get('youtube')
        copyright = request.POST.get('copyright')


        footer.address = address
        footer.phone_number = phone_number
        footer.email = email
        footer.facebook = facebook
        footer.instagram = instagram
        footer.twitter = twitter
        footer.youtube = youtube
        footer.copyright = copyright

        footer.save()
        return redirect('/create_footer')

    return render(request, 'admin/edit_footer.html', {'footer': footer, 'footer_id': footer_id, 'form':form})

@validate_request_for_admin
def delete_footer(request, footer_id):
    Footer.objects.filter(id=int(footer_id)).delete()
    return redirect('/create_footer')

@validate_request_for_admin
def create_menu(request):
    form = MenuForm()
    if request.method == 'POST':
        menu_name = request.POST.get('menu_name').lower()
        menu_link = request.POST.get('menu_link')
        menu_position = request.POST.getlist('menu_position')[0]
        menu_type = request.POST.get('menu_type')
        menu_index = request.POST.get('menu_index')
        image = request.FILES.get('image')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')

        data = dict(menu_name=menu_name, menu_link=menu_link,
                    menu_position=menu_position, menu_type=menu_type, 
                    menu_index=menu_index, image=image, short_content=short_content, long_content=long_content)
        Menu.objects.create(**data)
        return HttpResponseRedirect('/create_menu')
    header_footer = header_footer_view(request)
    menu = Menu.objects.all().order_by('created_at')
    data = {'menu': menu, 'form':form}
    data.update(header_footer)
    return render(request, 'admin/create_menu.html', data)

@validate_request_for_admin
def edit_menu(request, menu_id):
    form = MenuForm()
    menu = Menu.objects.get(id=int(menu_id))
    if request.method == 'POST':
        menu_name = request.POST.get('menu_name')
        menu_link = request.POST.get('menu_link')
        menu_position = request.POST.getlist('menu_position')
        image = request.FILES.get('image', None)
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')

        menu.menu_name = menu_name
        menu.menu_link = menu_link
        menu.short_content = short_content
        menu.long_content = long_content

        if image is not None:
            menu.image =image

        menu.save()
        return redirect('/create_menu')
    return render(request, 'admin/edit_menu.html', {'menu': menu, 'menu_id': menu_id, 'form':form})

@validate_request_for_admin
def delete_menu(request, menu_id):
    Menu.objects.filter(id=int(menu_id)).delete()
    return redirect('/create_menu')

@validate_request_for_admin
def create_sub_menu(request):
    form = SubMenuForm()
    menu_names = Menu.objects.all().values('menu_name').distinct()
    if request.method == 'POST':
        sub_menu_name = request.POST.get('sub_menu_name').lower()
        link_name = request.POST.get('menu_link')
        image = request.FILES.get('image')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        menu_value = request.POST.getlist('menu')[0]
        menu_id = Menu.objects.filter(menu_name=menu_value)[0].id

        data = dict(sub_menu_name=sub_menu_name,link_name=link_name,
                    image=image, short_content=short_content, long_content=long_content, menu_id=int(menu_id))
        SubMenu.objects.create(**data)
        return redirect('/create_sub_menu')
    header_footer = header_footer_view(request)
    sub_menu = SubMenu.objects.all().order_by('created_at')
    data = {'sub_menu': sub_menu, 'menu_names':menu_names, 'form':form}
    data.update(header_footer)
    return render(request, 'admin/create_sub_menu.html', data)

@validate_request_for_admin
def edit_sub_menu(request, sub_menu_id):
    form = SubMenuForm()
    sub_menu = SubMenu.objects.get(id=int(sub_menu_id))
    if request.method == 'POST':
        sub_menu_name = request.POST.get('sub_menu_name').lower()
        link_name = request.POST.get('menu_link')
        image = request.FILES.getlist('image', None)
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')

        sub_menu.sub_menu_name = sub_menu_name
        sub_menu.link_name = link_name
        sub_menu.short_content = short_content
        sub_menu.long_content = long_content

        if image is not None:
            sub_menu.image = image
        
        sub_menu.save()
        return redirect('/create_sub_menu')
    return render(request, 'admin/edit_sub_menu.html', {'sub_menu_id':sub_menu_id, 'sub_menu':sub_menu, 'form':form})

@validate_request_for_admin
def delete_sub_menu(request, sub_menu_id):
    SubMenu.objects.filter(id=int(sub_menu_id)).delete()
    return redirect('/create_sub_menu')

@validate_request_for_admin
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

@validate_request_for_admin
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

@validate_request_for_admin
def delete_banner(request, banner_id):
    Banner.objects.filter(id=int(banner_id)).delete()
    return HttpResponseRedirect('/create_banner')

@validate_request_for_admin
def create_about(request):
    form = AboutForm()
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
    return render(request, 'admin/create_about.html', {'about': about, 'form':form})

@validate_request_for_admin
def edit_about(request, about_id):
    form = AboutForm()
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
    return render(request, 'admin/edit_about.html', {'about': about, 'about_id': about_id, 'form':form})

@validate_request_for_admin
def delete_about(request, about_id):
    AboutSection.objects.filter(id=int(about_id))
    return redirect('/create_about')

@validate_request_for_admin
def create_news(request):
    form = NewsForm()
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
    return render(request, 'admin/create_news.html', {'news': news, 'form':form})

@validate_request_for_admin
def delete_news(request, news_id):
    News.objects.filter(id=int(news_id)).delete()
    return redirect('/create_news')

@validate_request_for_admin
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

@validate_request_for_admin
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

@validate_request_for_admin
def delete_gallery(request, gallery_id):
    Gallery.objects.filter(id=int(gallery_id)).delete()
    return redirect('/create_gallery')

@validate_request_for_admin
def create_blog(request):
    form = BlogForm()
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
    return render(request, 'admin/create_blog.html', {'blog': blog, 'form':form})

@validate_request_for_admin
def edit_blog(request, blog_id):
    form = BlogForm()
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
    return render(request, 'admin/edit_blog.html', {'blog': blog, 'blog_id': blog_id, 'form':form})

@validate_request_for_admin
def delete_blog(request, blog_id):
    Blog.objects.filter(id=int(blog_id)).delete()
    return redirect('/create_blog')

@validate_request_for_admin
def create_testimonial(request):
    form = TestimonialForm()
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
    return render(request, 'admin/create_testimonial.html', {'testimonial': testimonial, 'form':form})

@validate_request_for_admin
def edit_testimonial(request, test_id):
    form = TestimonialForm()
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
    return render(request, 'admin/edit_testimonial.html', {'testimonial': testimonial, 'test_id': test_id, 'form':form})

@validate_request_for_admin
def delete_testimonial(request, test_id):
    Testimonial.objects.filter(id=int(test_id)).delete()
    return redirect('/create_testimonial')

@validate_request_for_admin
def create_popup(request):
    form = PopupForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        message = request.POST.get('message')

        data = dict(title=title, file=file, message=message)
        if(Popup.objects.all().count() >= 1):
            messages.warning(request, "You can create only one popup")
            return HttpResponseRedirect('/create_popup')
        Popup.objects.create(**data)
        return redirect('/create_popup')
    popup = Popup.objects.all().order_by('created_at')
    return render(request, 'admin/create_popup.html', {'popup': popup, 'form':form})

@validate_request_for_admin
def edit_popup(request, popup_id):
    form = PopupForm()
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
    return render(request, 'admin/edit_popup.html', {'popup': popup, 'popup_id': popup_id, 'form':form})

@validate_request_for_admin
def delete_popup(request, popup_id):
    Popup.objects.filter(id=int(popup_id)).delete()
    return redirect('/create_popup')

@validate_request_for_admin
def inquiry_forms(request):
    inquiry_form = AdmissionForm.objects.all().order_by('created_at')
    return render(request, 'admin/inquiry_form.html', {'inquiry_form':inquiry_form})

@validate_request_for_admin
def delete_form(request, form_id):
    AdmissionForm.objects.filter(id=int(form_id)).delete()
    return redirect('/inquiry_form')


# client pages.....................
# ......................
# ..............................
# ....................

def pages(request, page_id):
    datas = Menu.objects.get(id=int(page_id))
    data = {
        'data': datas,
    }
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/main_page.html', data)

@api_view(['GET'])
def get_menu(request):
    menu = Menu.objects.all()
    # print("Menu list:", menu)
    data = []
    
    for m in menu:
        data.append(
            {
                'id':m.id,
                'menu_name':m.menu_name,
                'menu_link':m.menu_link,
                'menu_position':m.menu_position,
                'menu_type':m.menu_type,
                'menu_index':m.menu_index,
            }
        )
    return JsonResponse({'success':True, 'data':data})


@api_view(['GET'])
def get_sub_menu(request):
    # sub_menu = SubMenu.objects.get(id=int(menu_id))
    sub_menu = SubMenu.objects.all()
    data = []

    for sm in sub_menu:
        image = request.META['HTTP_HOST'] + '/' + \
            sm.image.url if sm.image else None
        data.append(
            {
                'id':sm.id,
                'sub_menu_name':sm.sub_menu_name,
                'link_name':sm.link_name,
                'short_content':sm.short_content,
                'long_content':sm.long_content,
                'image':image,
                'menu_id':sm.menu.id,
                'menu_type':sm.menu.menu_type,
            }
        )
    return JsonResponse({'success':True, 'data':data})

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
    data = {'footer': footer}
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

def sub_menu(request, sub_menu_id):
    sub_menu = SubMenu.objects.get(id=int(sub_menu_id))
    # print("sub menu link", sub_menu.link_name)
    # print("sub menu desc", sub_menu.short_content)
    data = {
        'sub_menu_data':sub_menu
    }
    header_footer = header_footer_view(request)
    data.update(header_footer)
    return render(request, 'client/sub_menu.html', data)