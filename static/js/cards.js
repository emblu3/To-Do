jQuery(function($) {
    $('.flipper').click(function() {
         $(this).parent().parent().toggleClass('is-flipped');
    });
  });