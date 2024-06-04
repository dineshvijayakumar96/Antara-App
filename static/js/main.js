// GSAP Animation
import { gsap } from "https://cdn.skypack.dev/gsap@3.11.4";
        import splitType from "https://cdn.skypack.dev/split-type@0.3.3";

        const ourText = new splitType('.text-animate-2', { types: 'chars' })
        const chars = ourText.chars

        gsap.fromTo(
        chars,
        { 
            y: 100,
            opacity: 0
        },
        {
            y: 0,
            opacity: 1,
            stagger: 0.02,
            duration: 0.4,
            ease: 'power1.out',
            delay: 0.8,
        }
        )

        function createAnimation(element) {
            // console.log('Creating animation for:', element);
            const ourText = new splitType(element, { types: 'chars' });
            const chars = ourText.chars;
        
            return gsap.fromTo(
                chars,
                {
                    y: 100,
                    opacity: 0,
                    delay: 0,
                },
                {
                    y: 0,
                    opacity: 1,
                    stagger: 0.01,
                    duration: 0.5,
                    ease: 'power1.out',
                    delay: 1,
                }
            );
        }
        
        const observerText = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const animation = createAnimation(entry.target);
                    animation.play();
                    observerText.unobserve(entry.target);
                }
            });
        });
        
        const elements = document.querySelectorAll('.text-animate');
        elements.forEach((element) => {
            observerText.observe(element);
        });        

        // --------------------------

        gsap.registerPlugin(ScrollTrigger);

        function createScrollAnimation(sectionSelector) {
            var tl = gsap.timeline();

            tl.from(sectionSelector, {
                duration: 0.5,
                ease: "power1.Out",
                xPercent: -100,
                opacity: 0,
            });

            tl.to(sectionSelector, {
                duration: 1,
                ease: "power1.Out",
                xPercent: 0,
                opacity: 1,
            });

            ScrollTrigger.create({
                trigger: sectionSelector,
                start: "top center",
                end: "center center",
                animation: tl,
            });
        }

        // Apply the function to multiple sections
        createScrollAnimation(".section1");
        createScrollAnimation(".section2");
        createScrollAnimation(".section3");

        function createScrollAnimation2(sectionSelector) {
            var tl = gsap.timeline();

            tl.from(sectionSelector, {
                duration: 0.5,
                ease: "power1.Out",
                xPercent: 100,
                opacity: 0,
            });

            tl.to(sectionSelector, {
                duration: 1,
                ease: "power1.Out",
                xPercent: 0,
                opacity: 1,
            });

            ScrollTrigger.create({
                trigger: sectionSelector,
                start: "top center",
                end: "center center",
                animation: tl,
            });
        }

        // Apply the function to multiple sections
        createScrollAnimation2(".section4");

        gsap.from(".service-title-box-bg", {
            duration: 0.5,
            ease: "power1.Out",
            xPercent: -100,
        });

        gsap.to(".service-title-box-bg", {
            duration: 1,
            ease: "power1.Out",
            xPercent: 0,
        });
        
        // gsap.from("nav", {
        //     ease: "power1.Out",
        //     yPercent: -100,
        // });

        // gsap.to("nav", {
        //     duration: 1,
        //     ease: "power1.Out",
        //     yPercent: 0,
        // });

        // gsap.from(".home-enq-appointment", {
        //     ease: "power1.Out",
        //     opacity: 0,
        // });

        // gsap.to(".home-enq-appointment", {
        //     duration: 1,
        //     ease: "none",
        //     opacity: 1,
        // });

        function createScrollAnimation3(sectionSelector) {
            var tl = gsap.timeline();

            tl.from(sectionSelector, {
                duration: 0,
                ease: "power1.Out",
                yPercent: 100,
                opacity: 0,
            });

            tl.to(sectionSelector, {
                duration: 1,
                ease: "power1.Out",
                yPercent: 0,
                opacity: 1,
            });

            ScrollTrigger.create({
                trigger: sectionSelector,
                start: "center center",
                end: "center center",
                animation: tl,
                // markers: true,
            });
        }

        // Apply the function to multiple sections
        createScrollAnimation3(".title-border-ani-0");
        createScrollAnimation3(".title-border-ani-1");
        createScrollAnimation3(".title-border-ani-2");
        createScrollAnimation3(".title-border-ani-3");
        createScrollAnimation3(".title-border-ani-4");
        createScrollAnimation3(".title-border-ani-5");
        createScrollAnimation3(".title-border-ani-6");
        createScrollAnimation3(".title-border-ani-7");
        createScrollAnimation3(".title-border-ani-8");


// GSAP Animation ends

/********** Sidenav Open/Close **********/
document.addEventListener('DOMContentLoaded', function () {
    const openNavElement = document.getElementById('opennav');
    const mySidenavElement = document.getElementById('mySidenav');

    openNavElement.addEventListener('click', function () {
        // Toggle the width of the navigation menu
        mySidenavElement.style.width = (mySidenavElement.style.width === '100%') ? '0' : '100%';
        mySidenavElement.style.opacity = (mySidenavElement.style.opacity === '1') ? '0' : '1';
        
        // Toggle the active class for the burger button
        openNavElement.classList.toggle('active');
    });
});

// Owl Carousel (Home Slider)
$(document).ready(function() {
    $("#owl-carousel").owlCarousel({
        touchDrag:true,
        loop:true,
        autoplaySpeed: 1000,
        autoplay:true,
        autoplayTimeout:2500,
        autoplayHoverPause:false,
        items: 1
    });
});

// Owl Carousel 2 (Steps to Apply)
$(document).ready(function() {
    $("#owl-carousel-2").owlCarousel({
        stagePadding: 0,
        singleItem:true,
        loop:false,
        nav:false,
        lazyLoad: true,
        margin: 10,
        responsiveClass: true,
        autoHeight: true,
        items: 1
    });
});

// Owl Carousel (Home Slider)
$(document).ready(function() {
    $("#owl-carousel-3").owlCarousel({
        touchDrag:true,
        loop:true,
        margin:10,
        items: 1
    });
});

// Owl Carousel (Home Slider)
$(document).ready(function() {
    $("#owl-carousel-3-3").owlCarousel({
        touchDrag:true,
        loop:true,
        margin:10,
        items: 1
    });
});

// Owl Carousel (Home Rates - Slider)
$(document).ready(function() {
    $("#owl-carousel-4").owlCarousel({
        touchDrag:true,
        loop:true,
        margin:10,
        items: 1
    });
});

// Owl Carousel (Home Rates - Slider)
$(document).ready(function() {
    $("#owl-carousel-5").owlCarousel({
        touchDrag:true,
        loop:true,
        margin:10,
        items: 1
    });
});

// Testimonials
var galleryThumbs = new Swiper('.gallery-thumbs', {
	effect: 'coverflow',
	grabCursor: true,
	centeredSlides: true,
	slidesPerView: '2',
	// coverflowEffect: {
	//   rotate: 50,
	//   stretch: 0,
	//   depth: 100,
	//   modifier: 1,
	//   slideShadows : true,
	// },
	
	coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 8,
        slideShadows : false,
	  },
	  
  });
  
var galleryTop = new Swiper('.swiper-container.testimonial', {
	speed: 1000,
	spaceBetween: 50,
	autoplay: {
	  delay: 3000,
	  disableOnInteraction: false,
	},
	direction: 'vertical',
	pagination: {
	  clickable: true,
	  el: '.swiper-pagination',
	  type: 'bullets',
	},
	thumbs: {
		swiper: galleryThumbs
	  }
  });
  