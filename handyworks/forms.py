from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import User

#Your forms here
class NewUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email')



