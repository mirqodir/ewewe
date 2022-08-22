from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser  
		fields = ('Ism','Tel','Pochta','Xabar',)


class CustomUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm):
		model = CustomUser  
		fields = ('Ism','Tel','Pochta','Xabar',)