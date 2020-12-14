from django.contrib import admin

from toys.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address']


@admin.register(Address)
class UserAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'zip_code', 'country']


@admin.register(Toy)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']


@admin.register(Tag)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
