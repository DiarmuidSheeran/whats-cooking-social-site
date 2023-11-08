# Manual Testing :man_mechanic:

#### As the developer, I conducted extensive testing along with the invaluable feedback from friends and family to ensure the site's features functioned flawlessly.
#### The project's user stories detailed the features that needed to be tested. Below, you'll find a list of the user stories, the issues they encompassed, and their corresponding grades after testing.
![]( "")
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

## User Story Issue: Add Comments to Posts
#### Problem Statement: 
* As a registered user, I can comment on posts so that I can interact with and express my opinion with users about their posts.
### Test:
* **Test users can comment on posts:**

![Commet Entered](documentation/testing/comments/Comment-entered-1.png "comment-entered")
![Comment Entered Succesfully](documentation/testing/comments/Comment-entered-2.png "succesfull-comment")

### Result:
* **Pass** :ok_hand:

### Test:
* **Test posts with +2 or more comments have view more link:**

![View More](documentation/testing/comments/Comment-entered-3-view-more.png "view-more-on-post")
![View More Link](documentation/testing/comments/Comment-entered-4-view-more-click.png "view-more-link-successfull")

### Result:
* **Pass** :ok_hand:

## :technologist: Overall Result:
* The User can successfully submit comments onto posts. They are succesfully redirected to the posts page. They can only see 2 comments per post on their feeds and can click view more to see all comments on the posts page.

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:

## User Story Issue:



