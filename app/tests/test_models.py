from django.test import TestCase
from django.contrib.auth.models import User
from app.models import UserProfile, Post, Comment


class ModelTestCase(TestCase):
    def setUp(self):
        # Given: Two user instances for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )

    def test_user_profile_creation(self):
        # Given: User profile data and an existing user
        user_profile = UserProfile.objects.create(
            user=self.user,
            fname='Sammy',
            lname='Sheeran',
            bio='Test bio',
            twitter='https://twitter.com/testuser',
            instagram='https://instagram.com/testuser',
            facebook='https://facebook.com/testuser',
        )
        # Then: Assert that user profile attributes are correctly set
        self.assertEqual(user_profile.user.username, 'testuser')
        self.assertEqual(str(user_profile), 'Sammy Sheeran')

    def test_post_creation(self):
        # Given: Post data and an existing user
        post = Post.objects.create(
            title='Test Post',
            user=self.user,
            content='This is a test post content'
        )
        # Then: Assert that post attributes are correctly set
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.user.username, 'testuser')
        self.assertTrue(post.slug)

    def test_comment_creation(self):
        # Given: Post data, user, and comment data
        post = Post.objects.create(
            title='Test Post',
            user=self.user,
            content='This is a test post content'
        )
        comment = Comment.objects.create(
            post=post,
            user=self.user,
            content='This is a test comment'
        )
        # Then: Assert that the comment is correctly represented
        self.assertEqual(str(comment), 'Comment by testuser on Test Post')
