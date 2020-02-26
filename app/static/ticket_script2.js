$(document).ready(function(){
      
	$(".placeholderanimation").each(function(){
		$(this).one("keypress",function(){
			$(this).addClass("active");
		});
	});
  
});
