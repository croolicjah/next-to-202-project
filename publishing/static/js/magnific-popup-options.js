$(document).ready(function() {
  // MagnificPopup
	var magnifPopup = function() {
		$('.image-popup').magnificPopup({
			delegate: 'a',
			type: 'image',
			removalDelay: 300,
			mainClass: 'mfp-with-zoom  mfp-img-mobile',
			image: {
				verticalFit: true,
				titleSrc: function(item) {

					var caption = item.el.attr('data-title');

					var pinItURL = "https://pinterest.com/pin/create/button/";

					// Refer to https://developers.pinterest.com/pin_it/
					pinItURL += '?url=' + 'http://dimsemenov.com/plugins/magnific-popup/';
					pinItURL += '&media=' + item.el.attr('href');
					pinItURL += '&description=' +  caption;


					return caption + ' &middot; <a class="pin-it" href="'+pinItURL+'" target="_blank"><img src="https://assets.pinterest.com/images/pidgets/pin_it_button.png" /></a>';
				}
		},
			gallery:{
				enabled:true
			},
			zoom: {
				enabled: true, // By default it's false, so don't forget to enable it

				duration: 300, // duration of the effect, in milliseconds
				easing: 'ease-in-out', // CSS transition easing function

				// The "opener" function should return the element from which popup will be zoomed in
				// and to which popup will be scaled down
				// By defailt it looks for an image tag:
				opener: function(openerElement) {
				// openerElement is the element on which popup was initialized, in this case its <a> tag
				// you don't need to add "opener" option if this code matches your needs, it's defailt one.
				return openerElement.is('img') ? openerElement : openerElement.find('img');
				}
			}
		});
	};

	var linkMagnifPopup = function() {
		$('.image-popup-link').magnificPopup({
			delegate: 'a',
		    type: 'image',


			gallery:{
				enabled: true
			},
		});
	};

	var magnifVideo = function() {
		$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,

        fixedContentPos: false
    });
	};

	$('.mycaption').magnificPopup({
		type: 'image',
		closeBtnInside: false,
		mainClass: 'mfp-with-zoom mfp-img-mobile',




    gallery: {
      enabled: true
    },



    callbacks: {
      open: function() {
        this.wrap.on('click.pinhandler', '.pin-it', function(e) {

          // This part of code doesn't work on CodePen, as it blocks window.open
          // Uncomment it on your production site, it opens a window via JavaScript, instead of new page
          /*window.open(e.currentTarget.href, "intent", "scrollbars=yes,resizable=yes,toolbar=no,location=yes,width=550,height=420,left=" + (window.screen ? Math.round(screen.width / 2 - 275) : 50) + ",top=" + 100);


          return false;*/
        });
      },
      beforeClose: function() {
       //this.wrap.off('click.pinhandler');
      }
    }

	});




	// Call the functions 
	magnifPopup();
	linkMagnifPopup();
	magnifVideo();


});