$(document).ready(function ($) {
    $(".like-form").on("click", function(event) {
      event.preventDefault();
      var $form = $(this);
      var postSlug = $form.data('post-slug');
      var likeAction = $form.find('button').data('like-action');
  
      var url = '/index/' + postSlug + '/like/';
  
      $.ajax({
        type: 'POST',
        url: url, 
        data: {
          'slug': postSlug,
          'like_action': likeAction,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
    
          if (likeAction === 'like') {
       
            $form.find('button').data('like-action', 'unlike');
            $form.find('i').css('color', '#cc2b5e');
          } else {

            $form.find('button').data('like-action', 'like');
            $form.find('i').css('color', '#f0ebeb');
          }
          $form.find('.number-of-likes').text(data.likes_count);
        },
        error: function (data) {
          console.log('Error:', data);
        },
      });
    });
});