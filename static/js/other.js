$(document).ready(function () {
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

    // API call for Menu..................................
    // ......................................
    // var menuIdInSubMenu = [];

    $.when($.ajax("/get_menu"), $.ajax('/get_sub_menu')).done(function (menu, subMenu) {
        var mainMenu = menu[0].data;
        var subMenuList = subMenu[0].data;

        mainMenu.map(a => {
            if (a.menu_position === "topheader") {
                // return (
                $('.top-header').append(`<li class="nav-item"><a class="nav-link bottom-nav-link text-capitalize" href=${a.menu_link}>` + a.menu_name + '</a></li>')
                // )
            } else {
                if (a.menu_type === "dropdown") {
                    var mainMenuId = a.id;
                    console.log("menu id", mainMenuId);
                    var filteredSubMenu = subMenuList.filter((x) => x.menu_id === mainMenuId)
                    // return (
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
                        // menuIdInSubMenu.push(a.menu_id)
                        // if (a.menu_type === 'dropdown') {
                            // return (
                                $(`#submenu-${mainMenuId}`).append(`<li><a class="dropdown-item" href="http://127.0.0.1:8000/sub_menu/${b.id}">` + b.sub_menu_name + '</a></li>')
                            // )
                        // }
                    })
                    // )
                } else {
                    // return (
                    $('.bottom-header').append(
                        `<a class="dropdown-item" href="${a.menu_link}">`
                        + a.menu_name +
                        '</a>'
                    )
                    // )
                }
            }
        })
        console.log("new menu", mainMenu);
        console.log("new sub menu", subMenuList);
    });


    // $.ajax({
    //     url: "/get_menu",
    //     type: "GET",
    //     async: false,
    //     success: function (result) {
    //         if (result.success = true) {
    //             data = result.data;
    //             console.log("menu data:", data);
    //             var res = data.map(a => {
    //                 if (a.menu_position === "topheader") {
    //                     return (
    //                         $('.top-header').append(`<li class="nav-item"><a class="nav-link bottom-nav-link text-capitalize" href=${a.menu_link}>` + a.menu_name + '</a></li>')
    //                     )
    //                 } else {
    //                     if (a.menu_type === "dropdown") {
    //                         return (
    //                             $('.bottom-header').append(
    //                                 `<li class="nav-item drop-menu dropdown" id="${a.id}">
    //                                 <button type="button" class="nav-link bottom-nav-link text-capitalize dropdown-toggle input-id" 
    //                                 id="dropdown" data-bs-toggle="dropdown"
    //                                 aria-expanded="false">`
    //                                 + a.menu_name +
    //                                 '</button></li>'
    //                                 // `<div class="dropdown" id="${a.id}">
    //                                 // <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">`
    //                                 // + a.menu_name +
    //                                 // `</button>`
    //                             )
    //                         )
    //                     } else {
    //                         return (
    //                             $('.bottom-header').append(
    //                                 `<a class="dropdown-item" href="${a.menu_link}">`
    //                                 + a.menu_name +
    //                                 '</a>'
    //                             )
    //                         )
    //                     }
    //                 }
    //             })
    //         }
    //     },
    //     error: function (error) {
    //         console.log(error);
    //     }
    // });
    // console.log("datas", menuId, menuIdInSubMenu);

    // $('.drop-menu').click(function () {
    //     var menuId = $(this).attr("id");
    //     console.log('menu id', menuId);
    //     var filteredMenu =  subMenu.filter((x) => x.menu_id === menuId);
    //     var res = filteredMenu.map(a => {
    //         if (a.menu_type === 'dropdown') {
    //             return (
    //                 $('.drop-menu').append('<ul class="dropdown-menu" aria-labelledby="dropdown"><li><a class="dropdown-item" href="">' + a.sub_menu_name + '</a></li></ul>')
    //             )
    //         }
    //     })
    // });

    // $(document).on('click', '.dropdown', function(e){
    //     e.preventDefault();
    //     var menuId = $(this).attr("id");
    //     // console.log('menu id', menuId);
    //     // var filteredMenu =  subMenu.filter((x) => Number(x.menu_id) === Number(menuId));
    //     // var res = filteredMenu.map(a => {
    //     //     // if (a.menu_type === 'dropdown') {
    //     //         return (
    //     //             $(this).append(
    //     //                 '<ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1"><li><a class="dropdown-item" href="#">'
    //     //                  + a.sub_menu_name + 
    //     //                 '</a></li></ul></div>'
    //     //                 )
    //     //         )
    //     //     // }
    //     // })
    // })

    // var subMenu = [];
    // $.ajax({
    //     url: '/get_sub_menu',
    //     type: 'GET',
    //     success: function (result) {
    //         if (result.success = true) {
    //             subMenu = result.data;
    //             data = result.data;
    //             console.log("sub menu:", data)
    //             var res = data.map(a => {
    //                 // menuIdInSubMenu.push(a.menu_id)
    //                 if (a.menu_type === 'dropdown') {
    //                     return (
    //                         $('.drop-menu').append(`<ul class="dropdown-menu" aria-labelledby="dropdown"><li><a class="dropdown-item" href="http://127.0.0.1:8000/sub_menu/${a.id}">` + a.sub_menu_name + '</a></li></ul>')
    //                     )
    //                 }
    //             })
    //         }
    //     },
    //     error: function (error) {
    //         console.log(error)
    //     }
    // })

    // function gettingId(id) {
    //     return id;
    // }

    // function getSubMenu() {
    //     $.ajax({
    //         url: '/get_sub_menu',
    //         type: 'GET',
    //         success: function (result) {
    //             if (result.success = true) {
    //                 subMenu = result.data;
    //                 datas = result.data;
    //                 console.log("sub menu:", data)
    //                 var res = data.map(a => {
    //                     if (a.menu_type === 'dropdown') {
    //                         return (
    //                             $('.drop-menu').append('<ul class="dropdown-menu" aria-labelledby="dropdown"><li><a class="dropdown-item" href="">' + a.sub_menu_name + '</a></li></ul>')
    //                         )
    //                     }
    //                 })
    //             }
    //         },
    //         error: function (error) {
    //             console.log(error)
    //         }
    //     })
    // }
    // getSubMenu();
});
