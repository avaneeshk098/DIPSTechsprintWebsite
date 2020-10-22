/*!
    * Start Bootstrap - Grayscale v6.0.2 (https://startbootstrap.com/themes/grayscale)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
    */
   function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
    const csrftoken = getCookie('csrftoken');
    $('#signup-form').submit((event) => {
        event.preventDefault()
        email1 = $("#inputEmail").val()
        $.ajax({
            url: '/submail',
            type: "post",
            data: {
                email : email1,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            },
            headers: {'X-CSRFtoken': csrftoken},
            cache: false,
            success: function () {
                alert("Congratulations! You have successfully been added to the mailing list.")
                document.querySelector("#inputEmail").value = ""
            },
            error: function(){
                alert("Sorry, there was some error at the server side.")
            }
        });
    })

    
    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
                this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top - 70,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#mainNav",
        offset: 100,
    });

    $(document).ready(function(){
	$(window).scroll(function(){
  	var light_pos = $('#fist').offset().top;
    var light_height = $('#fist').height();
    var menu_pos = $('.container').offset().top;
    var menu_height = $('.container').height();
    var scroll = $(window).scrollTop();
    console.log('light',light_pos);
    console.log('menu',menu_pos);
    console.log('scroll',scroll);
    
    if(menu_pos > light_pos && menu_pos < (light_pos + light_height)) {
    	$('#mainNav').removeClass('menu_white');
      $('#mainNav').removeClass('menu_black');
    }
    else {
    	$('#mainNav').removeClass('menu_white');
      $('#mainNav').addClass('menu_black');
    }
    
  })
})

    $('.js-change').ready(function(){       
        var scroll_pos = 0;
        $('.js-change').scroll(function() { 
            scroll_pos = $(this).scrollTop();
            if(scroll_pos > 210) {
                $('.hvr-reveal').css('color', '#ffffff');
            } else {
                $('.hvr-reveal').css('color', '#000000');
            }
        });
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
(jQuery); // End of use strict

