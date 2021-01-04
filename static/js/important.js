// ************************
//            Preloader
// ************************
$(window).on('load', function() {
    var preloaderFadeOutTime = 500;

    function hidePreloader() {
        var preloader = $('.spinner-wrapper');
        setTimeout(function() {
            preloader.fadeOut(preloaderFadeOutTime);
        }, 500);
    }
    hidePreloader();
});
// ************************
//          END Preloader
// ************************



// ************************
//            ScrollToTop
// ************************
// const scrollup = document.querySelector(".scrollup");
// window.addEventListener("scroll", () => {
//     if (window.pageYOffset > 100) {
//         scrollup.classList.add("scrollToTopactive");
//     } else {
//         scrollup.classList.remove("scrollToTopactive");
//     }
// })

// ***************************
//            ScrollToTop END
// ***************************

const myform = document.querySelector(".myform");
myform.classList.add("visible");

$(document).ready(function(){
    $(".fullform").click(function(){
        myform.classList.remove("visible");
        myform.classList.remove("invisible");
        myform.classList.add("invisible");
        
    });
    $(".exapand_form").click(function(){
        myform.classList.remove("invisible");
        myform.classList.add("visible");
    });
  });

// $("#fullform").click(function formInvisible() { 

// });






// ************************
//            Navbar
// ************************
// jQuery to collapse the navbar on scroll
// $(window).on('scroll load', function() {
//     if ($(".navbar").offset().top > 60) {
//         $(".fixed-top").addClass("top-nav-collapse");
//         $(".navbar-brand").addClass("text-dark");
//     } else {
//         $(".fixed-top").removeClass("top-nav-collapse");
//         $(".navbar-brand").removeClass("text-dark");

//     }
// });



// closes the responsive menu on menu item click
// $(".navbar-nav li a").on("click", function(event) {
//     if (!$(this).parent().hasClass('dropdown'))
//         $(".navbar-collapse").collapse('hide');
// });
// ************************
//          END Navbar
// ************************



// ************************
//          END COUNTERUP
// ************************

// var section = document.querySelector('.numbers');
// var hasEntered = false;
// window.addEventListener('scroll', (e) => {
//     var shouldAnimate = (window.scrollY + window.innerHeight) >= section.offsetTop;

//     if (shouldAnimate && !hasEntered) {
//         hasEntered = true;

//         $('.value').each(function() {
//             $(this).prop('Counter', 0).animate({
//                 Counter: $(this).text()
//             }, {
//                 duration: 4000,
//                 easing: 'swing',
//                 step: function(now) {
//                     $(this).text(Math.ceil(now));
//                 }
//             });
//         });

//     }
// });




// ***************************
//          END COUNTERUP
// ****************************





// ***************************
//              SKILLBAR
// ****************************

// var skillsection = document.querySelector('.skills');
// var hasEnteredskill = false;
// window.addEventListener('scroll', (e) => {
//     var shouldAnimate = (window.scrollY + window.innerHeight) >= skillsection.offsetTop;

//     if (shouldAnimate && !hasEnteredskill) {
//         hasEnteredskill = true;


//         $(".progress-bar").each(function() {
//             $(this).find(".progress-content").animate({
//                 width: $(this).attr("data-percentage")
//             }, 2000);

//             $(this).find(".progress-number-mark").animate({
//                 left: $(this).attr("data-percentage")
//             }, {
//                 duration: 2000,
//                 step: function(now, fx) {
//                     var data = Math.round(now);
//                     $(this).find(".percent").html(data + "%");
//                 }
//             });
//         });
//     }
// });


// ***************************
//          END SkillBar
// ****************************


// *******************************
//          Scroll Animation 1
// *******************************

// var $animation_elements = $('.card');
// var $window = $(window);

// function check_if_in_view() {
//     var window_height = $window.height();
//     var window_top_position = $window.scrollTop();
//     var window_bottom_position = (window_top_position + window_height);

//     $.each($animation_elements, function() {
//         var $element = $(this);
//         var element_height = $element.outerHeight();
//         var element_top_position = $element.offset().top;
//         var element_bottom_position = (element_top_position + element_height);

//         //check to see if this current container is within viewport
//         if ((element_bottom_position >= window_top_position) &&
//             (element_top_position <= window_bottom_position)) {
//             $element.addClass('canimate');
//         }
//     });
// }

// $window.on('scroll resize', check_if_in_view);
// $window.trigger('scroll');

// *******************************
//          Scroll Animation 1 End
// *******************************

// *******************************
//          Slick Slider Examples
// *******************************

//  draggable: false, Can not be drag
// fade: !0, or fade: true, for fade Animation
//pauseOnHover:true, This will pause the animation


/**  Second Slider */



// *******************************
//          Slick Slider Example End
// *******************************


// *******************************
//          Current Year
// *******************************
var d = new Date();
var n = d.getFullYear();
// document.getElementById("year").innerHTML = n;
// *******************************
//          Current Year End
// *******************************