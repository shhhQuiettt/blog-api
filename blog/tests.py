from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from .models import Post, Tag, Author

# Create your tests here.


class PostModelCreatrionTest(TestCase):
    def test_when_valid_params_post_can_be_created(self):
        user = get_user_model().objects.create_user(
            email="asdf@asdf.com", password="12345", is_active=True
        )
        author = Author(user=user, first_name="Olo", last_name="Bolo")
        author.save()

        # Tags
        tag1 = Tag(name="Health")
        tag2 = Tag(name="Revolution")

        # Post
        title = "Why you shouldn't drink water"
        body = "Everybody who had drunk water ever, eventualy died"
        publish_at = timezone.now() + timedelta(days=14)

        post = Post(title=title, body=body, publish_at=publish_at, author=author)
        post.save()

        post.tags.set([tag1, tag2])

        self.assertEqual(Post.objects.count(), 1)


class PostModelUtilityTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Author
        user = get_user_model().objects.create_user(
            email="asdf@asdf.com", password="12345", is_active=True
        )
        author = Author(user=user, first_name="Olo", last_name="Bolo")
        author.save()

        # Tags
        tag1 = Tag(name="Health")
        tag2 = Tag(name="Revolution")

        # Post
        title = "Why you shouldn't drink water"
        body = "Everybody who had drunk water ever, eventualy died"
        publish_at = timezone.now() + timedelta(days=14)

        cls.post = Post(title=title, body=body, publish_at=publish_at, author=author)
        cls.post.save()
        cls.post.tags.set([tag1, tag2])

    def test_is_published_is_true_when_publish_at_in_the_past(self):
        self.post.publish_at = timezone.now() - timedelta(days=10)
        self.assertTrue(self.post.is_published)

    def test_is_published_is_false_when_publish_at_in_the_future(self):
        self.post.publish_at = timezone.now() - timedelta(days=10)
        self.assertFalse(self.post.is_published)
