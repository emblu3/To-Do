jQuery(document).ready(function($) {
    $('.flipper').click(function() { 
         $(this).parent().parent().addClass('is-flipped');
    });
  });
