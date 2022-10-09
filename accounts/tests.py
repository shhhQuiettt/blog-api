from django.test import TestCase
from .models import User

# Create your tests here.


class TestUserModel(TestCase):
    def test_create_user(self):
        email = "a@w.pl"
        password = "123"
        User.objects.create_user(email=email, password=password)

        self.assertEqual(User.objects.all().count(), 1)
        user = User.objects.get()

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser_when_superuser_set_to_false(self):
        email = "aw.pl"
        password = "123"
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email=email, password=password, is_superuser=False
            )

        self.assertEqual(User.objects.all().count(), 0)

    def test_create_superuser_when_valid_data(self):
        email = "a@w.pl"
        password = "123"
        User.objects.create_superuser(email=email, password=password)

        self.assertEqual(User.objects.all().count(), 1)
        user = User.objects.get()

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
