$(document).ready(function () {
    const url = 'http://127.0.0.1:8000/';
    // const url = 'http://nasacollege.com/';
    imageDiv = $('#images').show();
    videoDiv = $('#videos').hide();
    $('#image_button').click(function () {
        imageDiv.show();
        videoDiv.hide();
    })
    $('#video_button').click(function () {
        imageDiv.hide();
        videoDiv.show();
    })
    $('.delete_banner').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_footer').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_menu').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_about').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_news').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_media').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_blog').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    })
    $('.delete_testimonial').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });
    $('.delete_popup').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });
    $('.delete-form').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });
    $('.delete_sub_menu').click(function () {
        if (!confirm("Are you sure you want to delete?")) {
            return false;
        }
    });

    $('#popup').modal('show');

    // API call for Menu..................................
    // ......................................
    // var menuIdInSubMenu = [];

    $.when($.ajax("/get_menu"), $.ajax('/get_sub_menu')).done(function (menu, subMenu) {
        var mainMenu = menu[0].data;
        var subMenuList = subMenu[0].data;

        mainMenu.map(a => {
            if (a.menu_position === "topheader") {
                $('.top-header').append(`<li class="nav-item"><a class="nav-link bottom-nav-link text-capitalize" href=${a.menu_link}>` + a.menu_name + '</a></li>')
            } else {
                if (a.menu_type === "dropdown") {
                    var mainMenuId = a.id;
                    console.log("menu id", mainMenuId);
                    var filteredSubMenu = subMenuList.filter((x) => x.menu_id === mainMenuId)
                    $('.bottom-header').append(
                        `<div class="nav-item drop-menu dropdown" id="${a.id}">
                            <button type="button" class="nav-link bottom-nav-link text-capitalize dropdown-toggle input-id" 
                            id="dropdown" data-bs-toggle="dropdown"
                            aria-expanded="false">`
                        + a.menu_name + '</button>' +
                        `<ul class="dropdown-menu" aria-labelledby="dropdown" id="submenu-${a.id}">` +
                        '</ul></div>'
                    )
                    filteredSubMenu.map(b => {
                        $(`#submenu-${mainMenuId}`).append(`<li><a class="dropdown-item text-capitalize" href="${url}sub_menu/${b.id}">` + b.sub_menu_name + '</a></li>')
                    })
                } else {
                    if (a.menu_link === null || a.menu_link === '') {
                        $('.bottom-header').append(
                            `<a class="nav-link text-capitalize bottom-nav-link text-dark" href="${url}nasacollege/${a.id}">`
                            + a.menu_name +
                            '</a>'
                        )
                    } else {
                        $('.bottom-header').append(
                            `<a class="nav-link text-capitalize bottom-nav-link text-dark" href="${url}${a.menu_link}">`
                            + a.menu_name +
                            '</a>'
                        )
                    }

                }
            }
        })
        console.log("new menu", mainMenu);
        console.log("new sub menu", subMenuList);
    });

    // main menu based on selected value....................
    var linkContent = $('.link-content').hide();
    $('#menu-type').change(function () {
        var val = $(this).val();
        if (val === 'link') {
            linkContent.show();
        } else {
            linkContent.hide();
        }
    })

    // Fixed header on scroll
    $(window).scroll(function () {
        var sticky = $('.sticky'),
            scroll = $(window).scrollTop();

        if (scroll >= 100) sticky.addClass('fixed');
        else sticky.removeClass('fixed');
    });


    // display video input link 
    var videoLink = $('.video-link').hide();
    var imageField = $('.image-field');
    $('#media-type').change(function(){
        var val = $(this).val();
        if (val === 'video'){
            videoLink.show();
            imageField.hide();
        }else{
            videoLink.hide();
            imageField.show();
        }
    });
});