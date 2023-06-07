$(document).ready(function(){


    let scrollLink = $(".scroll");

    //smooth scrolling
    scrollLink.click(function(e)
    {
        // e.preventDefault();
        $("body, html").animate({scrollTop : $(this.hash).offset().top
        }, 700);
    })


    

});