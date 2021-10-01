from django.contrib.auth import get_user_model
from django.db.models.expressions import Value
from django.test import TestCase

# Create your tests here.
class UserManagerTest(TestCase):
	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(email='carpenter@user.com', password='foo')
		self.assertEqual(user.email, 'carpenter@user.com')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)
		try:
			self.assertIsNone()(user.username)
		except AttributeError:
			pass
		with self.assertRaises(TypeError):
			User.objects.create_user()
		with self.assertRaises(TypeError):
			User.objects.create_user(email='')
		with self.assertRaises(ValueError):
			User.objects.create_user(email='', password="foo")