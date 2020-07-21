from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@test.fi'
        password = 'Pass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_noramlization(self):
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(email, 'modeltest12')
        # No need to test password

        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'modeltest12')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@test.fi',
            'test12'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
