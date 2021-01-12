from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from toys.models import Toy, Tag, User, Company, Employee, Address
from toys.services.send_weekly_report import send_weekly_toys_count, send_month_employees_salary


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1
    readonly_fields = ('password_change_link',)

    def password_change_link(self, obj):
        return format_html(f'<a href="/admin/toys/user/{obj.pk}/password/">Change Password<a/>')


def send_month_email_report(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, 'Multiple user selected, please choose one and only one.',
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())
    company = queryset.first()
    if not company.company_email:
        modeladmin.message_user(request, 'Selected company does not have email address',
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())
    send_month_employees_salary(company)
    modeladmin.message_user(request, 'Weekly report sent to user email: %s' % company.company_email, messages.INFO)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]
    list_display = ['company_name']
    actions = [send_month_email_report]


class UserToysInline(admin.StackedInline):
    model = Toy
    extra = 1


def send_weekly_email_report(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, 'Multiple user selected, please choose one and only one.',
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())
    user = queryset.first()
    if not user.email:
        modeladmin.message_user(request, 'Selected user does not have email address',
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())
    send_weekly_toys_count(user)
    modeladmin.message_user(request, 'Weekly report sent to user email: %s' % user.email, messages.INFO)

    return HttpResponseRedirect(request.get_full_path())


def send_month_email_report(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, 'Multiple user selected, please choose one and only one.',
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())
    company = queryset.first()
    company_name = queryset.first()
    if not company.company_email:
        modeladmin.message_user(request, 'Selected company does not have email address',
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())
    send_month_employees_salary(company, company_name)
    modeladmin.message_user(request, 'Weekly report sent to user email: %s' % company.company_email, messages.INFO)

    return HttpResponseRedirect(request.get_full_path())


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone', 'password_change_link']
    empty_value_display = '-'
    readonly_fields = ('password_change_link',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'password_change_link')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [UserToysInline]
    actions = [send_weekly_email_report]

    def password_change_link(self, obj):
        return format_html(f'<a href="/admin/toys/user/{obj.pk}/password/">Change Password<a/>')


class ToyTagsModelInline(admin.TabularInline):
    model = Toy.tags.through


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'description', 'price']
    search_fields = ['name', 'description']
    inlines = [ToyTagsModelInline]
    autocomplete_fields = ['tags']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'street', 'zip_code']
