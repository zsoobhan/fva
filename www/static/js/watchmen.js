$('#contact-js').on('click', function() {
  ga('send', 'event', 'contact', 'click', $(this).data('target'));
});

$('.social-icon-js').on('click', function() {
  ga('send', 'event', 'social', 'click', $(this).data('target'));
});
