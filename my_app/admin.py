from django.contrib import admin
from .models import Mebel
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm

# class CustomUserAdmin(UserAdmin):
# 	add_form = CustomUserCreationForm
# 	form = CustomUserChangeForm
# 	model = CustomUser



admin.site.register(Mebel)
# admin.site.register(CustomUser)
# admin.site.register(CustomUserAdmin)
