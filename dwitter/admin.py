from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile

# Serve para adicionar o Profile dentro da View de usuário no painel de Admin
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# admin.site.register(Profile)

# Register your models here.
