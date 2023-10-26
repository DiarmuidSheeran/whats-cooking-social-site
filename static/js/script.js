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

$(document).ready(function ($) {
  $(".follow-form").on("click", function(event) {
      event.preventDefault();
      var $form = $(this);
      var username = $form.data('username');
      var followAction = $form.find('button').data('follow-action');

      if (followAction === 'follow') {
        $form.find('button').data('follow-action', 'unfollow');
        $form.find('.follow-btn').text('Unfollow');
      } else {
        $form.find('button').data('follow-action', 'follow');
        $form.find('.follow-btn').text('Follow');
      }

      var url = '/index/' + username + '/follow/';

      $.ajax({
          type: 'POST',
          url: url,
          data: {
              'follow_action': followAction,
              'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function (data) {
            console.log('AJAX success callback');   
          },
          error: function (data) {
              console.log('Error:', data);
          },
      });
  });
});