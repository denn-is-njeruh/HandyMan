from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

#Your class manager here
class UserManager(BaseUserManager):
  """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
  """
  def create_user(self,email, password, **extra_fields):
    """
      Create and save a User with the given email and password.
    """
    if not email:
      raise ValueError('User must set an email to proceed')
    #extra_fields.setdefault('is_superuser',False)
    email = self.normalize_email(email)
    user = self.model(email=email,**extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user