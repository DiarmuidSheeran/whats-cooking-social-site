$(document).ready(function ($) {
  //Create Event handler for elements within class like-form
    $(".like-form").on("click", function(event) {
      // Prevents default actions being run
      event.preventDefault();
      //stores the clicked elements in $form variable
      var $form = $(this);
      // Gets the post's slug from the data attribute in the template
      var postSlug = $form.data('post-slug');
      // get like action from the button in the template
      var likeAction = $form.find('button').data('like-action');
      // URL constructed to follow same format as urls.py format
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
            // if the action was 'like', update the button data and icon color
            $form.find('button').data('like-action', 'unlike');
            $form.find('i').css('color', '#cc2b5e');
          } else {
            // if the action was 'unlike', update the button data and icon color
            $form.find('button').data('like-action', 'like');
            $form.find('i').css('color', '#f0ebeb');
          }
           // Updates the number of likes on the template with data from database
          $form.find('.number-of-likes').text(data.likes_count);
        },
        //logs error's to the console
        error: function (data) {
          console.log('Error:', data);
        },
      });
    });
});

$(document).ready(function ($) {
  //Create Event handler for elements within class follow-form
  $(".follow-form").on("click", function(event) {
    // Prevents default actions being run
      event.preventDefault();
      //stores the clicked elements in $form variable
      var $form = $(this);
      // Gets the username from the data attribute in the template
      var username = $form.data('username');
      // get follow-action from the button in the template and store in followaction variable
      var followAction = $form.find('button').data('follow-action');

      // Toggles between Follow and Unfollow in template
      if (followAction === 'follow') {
        $form.find('button').data('follow-action', 'unfollow');
        $form.find('.follow-btn').text('Unfollow');
      } else {
        $form.find('button').data('follow-action', 'follow');
        $form.find('.follow-btn').text('Follow');
      }
      // URL constructed to follow same format as urls.py format
      var url = '/index/' + username + '/follow/';

      $.ajax({
          type: 'POST',
          url: url,
          data: {
              'follow_action': followAction,
              'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
          },
          // Tests added for console callbacks to ensure working functionality
          success: function (data) {
            console.log('AJAX success callback');   
          },
          error: function (data) {
              console.log('Error:', data);
          },
      });
  });
});