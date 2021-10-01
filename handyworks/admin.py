from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserCreationForm,ExistingUserChangeForm
from .models import User

# Register your models here.
class NewUserAdmin(UserAdmin):
	add_form = NewUserCreationForm
	form = ExistingUserChangeForm
	model = User
	list_display = ('email','is_staff','is_active',)
	list_filter = ('email', 'is_staff','is_active',)
	fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)


admin.site.register(User, NewUserAdmin)