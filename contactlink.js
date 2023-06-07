$(document).ready(function(){


    if ($(window).width() > 1000) {
    $("#contact").click(function()
    {

        $('html ,body').animate({scrollTop : 6660},800);
    });


}
    else {
        $("#contact").click(function()
    {

        $('html ,body').animate({scrollTop : 25500},800);
    });
    
    }



});
