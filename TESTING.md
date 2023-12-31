# Automated Testing :man_mechanic:

#### As part of my project I decided to implement some automated testing into my project.

#### Unit testing was employed for automated testing, encompassing the examination of URLs, models, forms, and views. The testing process resulted in an attainment of 72% coverage. The comprehensive coverage report is as follows:

![Automated Test](documentation/testing/automated-testing/test-ran.png "automated-test")
![Coverage Report](documentation/testing/automated-testing/coverage-report.png "coverage-report")

# Manual Testing :man_mechanic:

#### As the developer, I conducted extensive testing along with the invaluable feedback from friends and family who signed up to the site to ensure the site's features functioned as flawlessly as possible.
#### The project's user stories detailed the features that needed to be tested. Below, you'll find a list of the user stories, the issues they encompassed, and their corresponding grades after testing.

## User Story Issue: User Registration and Authentication
#### Problem Statement: 
* As a site user I can login or create an account and logout so that I can view my content and other users content and choose to logout when finished. 
### Test:
* **Test signup with errors:**

![sign-up error](documentation/testing/signup/signup-with-errors.png "sign-up-error")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test succesfull signup:**

![Entered-Details](documentation/testing/signup/signup-with-details.png "Entered-signup-details")
![Signup-success](documentation/testing/signup/signup-success.png "Signup-Success")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test login with errors:**

![Login-Errors](documentation/testing/login/login-error.png "Login-errors")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test succesful login:**

![Login-Details-entered](documentation/testing/login/login-with-user.png "Login-details")
![Login Success](documentation/testing/login/login-succesful.png "Login-Success")

### Result:
* **Pass** :ok_hand:

### Test:
* **User Can Logout:**

![Logout Button](documentation/testing/logout/logout-btn.png "Logout-btn")
![Logout Success](documentation/testing/logout/logout-success.png "Logout-success")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* User can succesfully sign up to create a new account. They can Login to their account and they can logout when needed. Appropriate error messages were displayed to users upon unsuccesfull or incomplete forms being submitted.

## User Story Issue: Create Posts.
#### Problem Statement:
* As a registered user, I can create posts so that I can share my content with the rest of the users on the site.
### Test:
* **Test users can can create posts**

![Create Post Buttons](documentation/testing/create-posts/create-post-1-btn.png "create-post-buttons")

![Create Post Form](documentation/testing/create-posts/create-post-2-form.png "create-post-form")
![Post Created Successfully](documentation/testing/create-posts/create-post-5-post-created.png "post-created-successfully")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test post creation errors wroking:**

![Error For Text Fields](documentation/testing/create-posts/create-post-3-form-error.png "error-for-text-field")
![Error for large file size](documentation/testing/create-posts/create-post-4-form-error-file-size.png "large-file-size-error")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* Users can create posts and the posts are correctly placed on users feeds and profiles. Error handling is succesfully used to catch users not entering all details into text fields. File sizes that are too large are prohibeted from being uploaded to the site an error handling succesfully disables users abilities to upload large files.

## User Story Issue: Update Posts
#### Problem Statement: 
* As a registered user, I can update my posts so that I can edit or delete my content.

### Test:
* **Test edit post button directs users to the correct post to edit:**

![Check Edit Button](documentation/testing/edit-posts/edit-post-1-btn.png "error-button-redirect")

![Redirect to Correct Post](documentation/testing/edit-posts/edit-post-2-form.png "error-button-redirect-success")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test updated form fields on post to see if the post updates with new content**

![Updated Form Fields](documentation/testing/edit-posts/edit-post-3-updated-form.png "updated-form-fields")

![Updated Form Fields Success](documentation/testing/edit-posts/edit-post-4-updated.png "updated-form-fields-success")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test delete button on post navigates to deletion warning page.**

![Navigate to delete post page](documentation/testing/edit-posts/edit-post-delete-page.png "navigate-to-post-deletion-page")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test delete button on warning page succesfully deletes post.**

![Post successfully deleted](documentation/testing/edit-posts/edit-post-delete-message.png "post-successfully-deleted")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can succesfully be directed to a post edit page and edit the post they desire. The user can change all fields within the post. The user can choose to delete the post at anytime and is issued with a warning before deleting the post.

## User Story Issue: Like Posts
#### Problem Statement:
* As a registered user, I can like or unlike posts so that I can interact with the content. of the site to enhance my experience.
### Test:
* **Test users can like or unlike posts, check that the like count of the posts changes:**

![Unliked Post](documentation/testing/like-posts/like-btn-not-clicked.png "unliked-post")

![Liked Post](documentation/testing/like-posts/like-btn-clicked.png "liked-post")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can succesfully click the like button on any post and heve their like recorded. Their count is added and the heart icon changes color. Alternatively the user click the button again to unlike the post and the button's count reverts back along with the icons color.

## User Story Issue: Add Comments to Posts
#### Problem Statement: 
* As a registered user, I can comment on posts so that I can interact with and express my opinion with users about their posts.
### Test:
* **Test users can comment on posts:**

![Commet Entered](documentation/testing/comments/comment-entered-1.png "comment-entered")
![Comment Entered Succesfully](documentation/testing/comments/comment-entered-2.png "succesfull-comment")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test posts with +2 or more comments have view more link:**

![View More](documentation/testing/comments/comment-entered-3-view-more.png "view-more-on-post")

![View More Link](documentation/testing/comments/comment-entered-4-view-more-click.png "view-more-link-successfull")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The User can successfully submit comments onto posts. They are succesfully redirected to the posts page. They can only see 2 comments per post on their feeds and can click view more to see all comments on the posts page.

## User Story Issue: Follow other Users & View Follower Counts
#### Problem Statement:
* As a registered user, I can like or unlike posts so that I can interact with the content. of the site to enhance my experience.

* As a registered user, I can view the total number of followers I have and the number of users I'm following so that I can monitor how my profile is doing. 
### Test:
* **Test users can follow or unfollow other users, Check that follower counts are updated on users profile, check user is added to following dropdown menu:**

![Unfollowed User](documentation/testing/follow-users/follow-btn-1-unclicked.png "unfollowed-users-btn")

![Followed User](documentation/testing/follow-users/follow-btn-1-clicked.png "followed-users")

![Followed User Counts](documentation/testing/follow-users/follow-btn-3-chack-follower-count.png "followed-users-counts")

![Followed User Dropdown Menu](documentation/testing/follow-users/follow-btn-4-chack-follower-dropdown.png "followed-users-dropdown")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can succesfully click the follow button on a users post and the button will be updated to a unfollow button. The unfollow button can be clicked and the user will unfollow the designated user. The Following count is updated on the users profile page. The followed or not followed user is added or deleted from the users following dropdown menu depending on choice selected.

## User Story Issue: Bio Section
#### Problem Statement:
* As a registered user, I can include a bio section so that I can share some personal details about me.
### Test:
* **Test users can successfully update their accounts bio from their profile page**

![Update Bio Button](documentation/testing/bio/update-bio-1-btn.png "update-bio-btn")

![Update Bio Form](documentation/testing/bio/update-bio-2-form.png "update-bio-form")

![Update Bio Form Details](documentation/testing/bio/update-bio-3-form-input.png "update-bio-form-details")

![Bio Updated](documentation/testing/bio/update-bio-4-updated-bio.png "bio-updated")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can succesfully click the bio button on their profile and they are redirected to update bio form page. The User can enter information into whatever fields the wish and click the update bio button. The User is redirected back to the profile page and their bio was succesfully updated.

## User Story Issue: Update or Delete User Information & Update Profile Picture
#### Problem Statement:
* As a registered user, I can edit or delete my profile information so that I can keep my personal information up to date and delete it if necessary.
* As a registered user, I can upload my own profile picture so that I can add personalisation to my profile.
### Test:
* **Test users can successfully update their account information:**

![Update Info Button](documentation/testing/account-info/update-info-1-btn.png "update-info-btn")

![Update Info Form Filled](documentation/testing/account-info/update-info-2-edit-info.png "update-info-form-filled")

![Update Info Success](documentation/testing/account-info/update-info-3-info-updated.png "update-info-success")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test users can update their profile picture:**

![Update Profile Pic Button](documentation/testing/account-info/update-profile-pic-1.png "update-pic-btn")

![Update Profile Pic Button Selected](documentation/testing/account-info/update-profile-pic-2.png "update-profile-pic-button")

![Update Profile Pic Success](documentation/testing/account-info/update-profile-pic-3.png "update-profile-pic-success")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test users can delete their account**

![Redirect to Delete Account Page](documentation/testing/account-info/delete-account-warning.png "delete-account-warning")

![Account deletion success](documentation/testing/account-info/account-deleted.png "account-updated-success")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can successfully update their account information, update their profile picture and delete their account. All of this can be achieved throught the settings page of the user account.

## User Story Issue: Search Capabilities
#### Problem Statement:
* As a registered user I can search for users within the site so that I can easily find other users on the site.

### Test:
* **Test users abbility to search for other users on the site:**

![User Search Bar](documentation/testing/search-user/search-users.png "user-search-bar")

![Search Bar Entered Data](documentation/testing/search-user/search-users-2-name.png "search-bar-data-entered")

![Search Results](documentation/testing/search-user/search-users-3-results.png "search-results")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can successfully search for other user profiles within the database.

## User Story Issue: View Recipes
#### Problem Statement:
* As a registered user, I can view recipe ideas by entering food I want to use so that I can get inspiration for new ideas for my content.

### Test:
* **Test users abbility to search for recipes by entering food groups intop search bar**

![Recipe Search Bar](documentation/testing/recipes/search-recipes.png "Recipe-search-bar")

![Recipe Bar Entered Data](documentation/testing/recipes/search-recipes-2-input.png "Recipe-bar-data-entered")

![Recipe Results](documentation/testing/recipes/search-recipes-3-results.png "Recipe-results")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can successfully search for recipes from the seacrh bar by entering a food group. The user can click on the recipe they like and will be directed to the recipes web page.

## User Story Issue: Reset Password
#### Problem Statement:
* As a registered user I can reset my password so that if I forget my password I can regain access to my account.

### Test:
* **Test users abbility to reset their password**

![ReSET Password Button](documentation/testing/reset-password/reset-password-1.png "reset-pwd-btn")

![Email Form Filled](documentation/testing/reset-password/reset-password-2-enter-email.png "email-form-filled")

![Email Sent Confirmation](documentation/testing/reset-password/reset-password-3-email-sent.png "email-sent-confirmation")

![Email Recieved](documentation/testing/reset-password/reset-password-4-email-recieved.png "password-reset-email")

![Password Reset Form](documentation/testing/reset-password/reset-password-5-reset-password-from-link.png "password-reset-form")

![Password reset confiremd](documentation/testing/reset-password/reset-password-6-reset-password-confirmed.png "password-reset-confiremed")

![New Password Test](documentation/testing/reset-password/reset-password-7-reset-password-working.png "new-password-test")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The user can successfully request a password reset to be sent to their email address. The email is delivered to the user. The User can click on the link provided in the email be directed to the password reset page. The user can reset their password and can access their account with their new password.

# Validators :man_mechanic:

* As Part of testing my site I tested my code on various validators. 
## W3Markup Html Validation
[A link to W3Markups website](https://validator.w3.org/)

* The images below repersent the source code of my templates passing the tests of the W3markup Validator

### Bio
![Validator Test](documentation/validator-results-html/bio.png "html-validator-test")

### Create Post
![Validator Test](documentation/validator-results-html/create-post.png "html-validator-test")

### Delete Post
![Validator Test](documentation/validator-results-html/delete-post.png "html-validator-test")

### Error 404
![Validator Test](documentation/validator-results-html/error-404.png "html-validator-test")

### Error 500
![Validator Test](documentation/validator-results-html/error-500.png "html-validator-test")

### Follow Feed
![Validator Test](documentation/validator-results-html/follow-feed.png "html-validator-test")

### Index/Home
![Validator Test](documentation/validator-results-html/index.png "html-validator-test")

### Landing
![Validator Test](documentation/validator-results-html/landing.png "html-validator-test")

### Login
![Validator Test](documentation/validator-results-html/login.png "html-validator-test")

### Password Reset Complete
![Validator Test](documentation/validator-results-html/password-reset-complete.png "html-validator-test")

### Password Reset Sent
![Validator Test](documentation/validator-results-html/password-reset-sent.png "html-validator-test")

### Password Reset
![Validator Test](documentation/validator-results-html/password-rest.png "html-validator-test")

### Post
![Validator Test](documentation/validator-results-html/post.png "html-validator-test")

### Recipes
![Validator Test](documentation/validator-results-html/recipes.png "html-validator-test")

### Settings
![Validator Test](documentation/validator-results-html/settings.png "html-validator-test")

### Sign up
![Validator Test](documentation/validator-results-html/signup.png "html-validator-test")

### Other User Profiles
![Validator Test](documentation/validator-results-html/un-auth-user-profile.png "html-validator-test")

### Update Info
![Validator Test](documentation/validator-results-html/update-info.png "html-validator-test")

### Update Post
![Validator Test](documentation/validator-results-html/update-post.png "html-validator-test")

### Search Results
![Validator Test](documentation/validator-results-html/user-search-results.png "html-validator-test")

### User Search
![Validator Test](documentation/validator-results-html/user-search.png "html-validator-test")

### User Profile
![Validator Test](documentation/validator-results-html/users-profile.png "html-validator-test")

## Ci Python Linter Python Code Validator
[A link to Ci python linter site](https://pep8ci.herokuapp.com/)

* The images below repersent the sites python code passing the tests of the Ci python linter Validator

### Decorator.py
![Validator Test](documentation/testing/validator-results-python/decorator-linter.png "python-validator-test")

### Forms.py
![Validator Test](documentation/testing/validator-results-python/forms-linter.png "python-validator-test")

### Models.py
![Validator Test](documentation/testing/validator-results-python/models-linter.png "python-validator-test")

### Settings.py
![Validator Test](documentation/testing/validator-results-python/settings-linter.png "python-validator-test")

### Forms Test
![Validator Test](documentation/testing/validator-results-python/test-foms-linter.png "python-validator-test")

### Models Test
![Validator Test](documentation/testing/validator-results-python/test-model-linter.png "python-validator-test")

### Urls Test
![Validator Test](documentation/testing/validator-results-python/test-urls-linter.png "python-validator-test")

### Views Test
![Validator Test](documentation/testing/validator-results-python/test-views-linter.png "python-validator-test")

### Urls.py
![Validator Test](documentation/testing/validator-results-python/urls-linter.png "python-validator-test")

### Views.py
![Validator Test](documentation/testing/validator-results-python/views-linter.png "python-validator-test")

## Js Hint Javascript Code Validator
[A link to Js Hint Javascript Validator Site](https://jshint.com/)

* The images below repersent the sites script code passing the tests of the Js hint Javascript Validator

### Script.js
![Validator Test](documentation/validator-results-script/script-validator.png "script-validator-test")

## Jigsaw Css Validator
[A link to Js Hint Css Validator Site](https://jigsaw.w3.org/css-validator/#validate_by_input)

* The images below repersent the sites styles code passing the tests of the Jigsaw Css Validator

### Styles.css
![Validator Test](documentation/validator-results-css/css-validation.png "css-validator-test")

# Lighthouse Tests 	:lighthouse:

* As Part of testing my site i put each of my templates through the lighthouse testing service on chromes dev tools the results can be seen below:

### Create Post-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/create-post-lighthouse.png "lighthouse-test")

### Delete-Account-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/delete-account-lighthouse.png "lighthouse-test")

### Delete Post-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/delete-post-lighthouse.png "lighthouse-test")

### Edit Post-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/edit-post-lighthouse.png "lighthouse-test")

### Follow Feed-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/follow-feed-lighthouse.png "lighthouse-test")

### Index/Home-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/index-lighthouse.png "lighthouse-test")

### Landing-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/landing-lighthouse.png "lighthouse-test")

### -Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/login-lighthouse.png "lighthouse-test")

### Non User Profile-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/non-users-profile.png "lighthouse-test")

### Password Reset Complete-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/password-reset-complete.png "lighthouse-test")

### Password Reset Complete-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/password-sent-lighthouse.png "lighthouse-test")

### Post-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/post-lighthouse.png "lighthouse-test")

### Recipe-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/recipe-search.png "lighthouse-test")

### Reset Password Form-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/reset-password-form.png "lighthouse-test")

### Reset Password-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/reset-password-lighthouse.png "lighthouse-test")

### Search Results-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/search-results-lighthouse.png "lighthouse-test")

### Settings-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/settings-lighthouse.png "lighthouse-test")

### Signup-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/signup-lighthouse.png "lighthouse-test")

### Update Bio-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/update-bio-lighthouse.png "lighthouse-test")

### Update Info-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/update-info-lighthouse.png "lighthouse-test")

### User Profile-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/user-profile-page-lighthouse.png "lighthouse-test")

### User Search-Lighthouse
![Lighthouse Results](documentation/testing/lighthouse-results/user-search-lighthouse.png "lighthouse-test")

