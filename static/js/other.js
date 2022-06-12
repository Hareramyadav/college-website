let i=2;
$(document).ready(function () {
    const url = 'http://127.0.0.1:8000/';
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
                    if (a.menu_link != '') {
                        $('.bottom-header').append(
                            `<a class="nav-link text-capitalize bottom-nav-link text-dark" href="${url}shalmani/${a.id}">`
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

    // footer based on selected value
    var footerFirst = $('.footer-first').show();
    var socialLinks = $('.social-links').hide();
    var copyright = $('.copyright').hide();
    $('#footer_position').change(function () {
        var val = $(this).val();
        if (val === 'footer_third') {
            footerFirst.hide();
            socialLinks.show();
        }
        if (val === 'copyright') {
            copyright.show();
            footerFirst.hide();
            socialLinks.hide();
        }
    })
    // news based on selected value
    var newsIdentity = $('.news-identity').hide();
    var news = $('.news').show();
    $('#news_position').change(function () {
        var val = $(this).val();
        if (val === 'news_identity') {
            newsIdentity.show();
            news.hide();
        } else {
            newsIdentity.hide();
            news.show();
        }
    })


    // circular loop.................

    var radius = 300;
    var fields = $('.circleItem');
    var container = $('.circleContent');
    var width = container.width();
    radius = width / 2.4;

    var height = container.height();
    var angle = 0, step = (2 * Math.PI) / fields.length;
    fields.each(function () {
        var x = Math.round(width / 2 + radius * Math.cos(angle) - $(this).width() / 2);
        var y = Math.round(height / 2 + radius * Math.sin(angle) - $(this).height() / 2);
        if (window.console) {
            console.log($(this).text(), x, y);
        }

        $(this).css({
            left: x + 'px',
            top: y + 'px'
        });
        angle += step;
    });


    // $('.itemDot').click(function () {

    //     var dataTab = $(this).data("tab");
    //     $('.itemDot').removeClass('active');
    //     $(this).addClass('active');
    //     $('.CirItem').removeClass('active');
    //     $('.CirItem' + dataTab).addClass('active');
    //     i = dataTab;

    //     $('.dotCircle').css({
    //         "transform": "rotate(" + (360 - (i - 1) * 36) + "deg)",
    //         "transition": "2s"
    //     });
    //     $('.itemDot').css({
    //         "transform": "rotate(" + ((i - 1) * 36) + "deg)",
    //         "transition": "1s"
    //     });


    // });

    // setInterval(function () {
    //     var dataTab = $('.itemDot.active').data("tab");
    //     if (dataTab > 9 || i > 9) {
    //         dataTab = 1;
    //         i = 1;
    //     }
    //     $('.itemDot').removeClass('active');
    //     $('[data-tab="' + i + '"]').addClass('active');
    //     $('.CirItem').removeClass('active');
    //     $('.CirItem' + i).addClass('active');
    //     i++;


    //     $('.dotCircle').css({
    //         "transform": "rotate(" + (360 - (i - 2) * 36) + "deg)",
    //         "transition": "2s"
    //     });
    //     $('.itemDot').css({
    //         "transform": "rotate(" + ((i - 2) * 36) + "deg)",
    //         "transition": "1s"
    //     });

    // }, 5000);
});
