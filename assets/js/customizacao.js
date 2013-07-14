jQuery(document).ready(function(){   
  /********************/
/*      MENU         */
/********************/ 

     
	var $content 		= $("body");
	
	// Run easytabs
  	$content.easytabs({
	  animate		: true,
	  updateHash		: true,
	  transitionIn		:'slideDown',
	  transitionOut		:'slideUp',
	  animationSpeed	:1000,
	  tabs			:".emenu",
	  tabActiveClass	:'active',
	});

 /*****************************************/
/*      FILTERING PORTFOLIO ITEMS         */
/******************************************/ 

	var 
	speed = 500,   // animation speed
	$wall = $('#masonry-wrapper').find('ul.filterable')
	;

	$wall.masonry({

	itemSelector: '.one:not(.invis),.one-half:not(.invis),.one-third:not(.invis),.one-fourth:not(.invis)',
	animate: true,
	animationOptions: {
	duration: speed,
	queue: false
	}
	});

	$('.filter a').click(function(){
	var colorClass = '.' + $(this).attr('class');

	if(colorClass=='.all') {
	// show all hidden boxes
	$wall.children('.invis')
	.toggleClass('invis').fadeIn(speed);
	} else {  
	// hide visible boxes 
	$wall.children().not(colorClass).not('.invis')
	.toggleClass('invis').fadeOut(speed);
	// show hidden boxes
	$wall.children(colorClass+'.invis')
	.toggleClass('invis').fadeIn(speed);
	}
	$wall.masonry();

	 return false;
	});

// EXTRA CODE FOR FILTER NAVIGATION

	$('.filter a').click(function() {
		$('.filter .active-nav').removeClass('active-nav');
		$(this).parent().addClass('active-nav');
	
		return false;
	});
// HOVER EFFECT FOR PORTFOLIO ITEMS
	
	$('.filterable li a img').css('opacity', '0.4');
	
	$('.filterable li a').hover(function(){
		
			$(this).find('img').stop().animate({opacity: '1'}, 600)
		},function(){
			$(this).find('img').animate({opacity: '0.4'}, 600)
		
	});
	
 /*****************************************/
/*      FANCYBOX                          */
/******************************************/
		$('a[rel=fancybox]').fancybox();
		

 /*****************************************/
/*     Validate and ajax submit for contact form                      */
/******************************************/
		$("#leave-message").validate({                    		
		submitHandler: function(form) {                    			
			$(form).ajaxSubmit({                    				
				target: '#contact-form-result',                                 
				success: function() {                                     
					$('#contact-form').fadeOut(500, function(){                                           
					$('#contact-form-result').fadeIn(500);                                        
					});                       
				},         
				error: function() { 
					$('#contact-form-result').fadeIn(500); 
				}  
			});          
		}                    
		}); 
});	