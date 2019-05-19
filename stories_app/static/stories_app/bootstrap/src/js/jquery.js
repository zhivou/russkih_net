$(document).ready(function(){
    $(".btn1").mouseover(function(){
        $("p").fadeOut()
    });
    $(".btn2").mouseover(function(){
        $("p").fadeIn();
    });
});

$(document).ready(function(){
    $("#navbarWrapper").mouseover(function(){
        $("#navbarContainer").animate({height: "300px"});
    });
    $("#mainPic").mouseover(function(){
        $("#navbarContainer").animate({height: "50px"});
    });
});
