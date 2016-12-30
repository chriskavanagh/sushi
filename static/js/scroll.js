//uses scrollTo plugin to scroll from Home (in Nav) to #target in footer.


$(function(){
    $('#nav-about').click(function() {
		$.scrollTo($('#about'), 2000);
	});
	$('#newsbutton').click(function() {
		$.scrollTo($('#below_map_row'), 2000);
	});
	$('#nav-contact').click(function() {
		$.scrollTo($('#above_map_row'), 2000);
	});
 });
 
 
