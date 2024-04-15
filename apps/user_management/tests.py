from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class UserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='will@gmail.com',
            first_name='Will',
            last_name='Claye',
            password='abc123'
        )
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertEqual(user.first_name, 'Will')
        self.assertEqual(user.last_name, 'Claye')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='superadmin@gmail.com',
            first_name='Super',
            last_name='Admin',
            password='abc123'
        )
        self.assertEqual(admin_user.email, 'superadmin@gmail.com')
        self.assertEqual(admin_user.first_name, 'Super')
        self.assertEqual(admin_user.last_name, 'Admin')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)