from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
         
    def test_new_user_email_normalized(self):
        email = 'test@Test.com'
        user = get_user_model().objects.create_user(email, 'Password123')
        self.assertEqual(user.email, email.lower())
        
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Password123')
            
    def test_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'Password123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        