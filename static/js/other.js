$(document).ready(function(){
    imageDiv = $('#images').show();
    videoDiv = $('#videos').hide();
    $('#image_button').click(function(){
        imageDiv.show();
        videoDiv.hide();
    })
    $('#video_button').click(function(){
        imageDiv.hide();
        videoDiv.show();
    })
    $('.delete_banner').click(function(){
        if(!confirm("Are you sure you want to delete?")){
            return false;
        }
    })
    $('.delete_footer').click(function(){
        if(!confirm("Are you sure you want to delete?")){
            return false;
        }
    })
    $('.delete_menu').click(function(){
        if(!confirm("Are you sure you want to delete?")){
            return false;
        }
    })
    $('.delete_about').click(function(){
        if(!confirm("Are you sure you want to delete?")){
            return false;
        }
    })
    $('.delete_news').click(function(){
        if(!confirm("Are you sure you want to delete?")){
            return false;
        }
    })
    $('.delete_testimonial').click(function(){
        if(!confirm("Are you sure you want to delete?")){
            return false;
        }
    })
});