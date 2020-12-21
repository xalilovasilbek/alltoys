from django.contrib import admin

from toys.models import Toy, Tag, User, Company, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class EmployeeInline(admin.TabularInline):
    model = Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]
    list_display = ['company_name']


admin.site.register(Toy)
admin.site.register(Tag)
admin.site.register(User)
