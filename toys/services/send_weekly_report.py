from django.core.mail import send_mail
from toys.models import Toy, Employee


def send_weekly_toys_count(user):
    toys_count = Toy.objects.filter(user=user, is_active=True).count()
    send_mail(
        'Yor toys update from AllToys!',
        f'You have {toys_count} active toys at the end of this week!',
        'info@alltoys.uz',
        [user.email],
        fail_silently=False,
    )


def send_month_employees_salary(company_name):
    employees_of_company = Employee.objects.filter(company__company_name=company_name)
    employees_salary = employees_of_company.values_list('salary', flat=True)
    sum_employees_salary = 0
    for i in employees_salary:
        sum_employees_salary = sum_employees_salary + i
    send_mail(
        'Your report update!',
        f'Your Company {sum_employees_salary} $ spent for salaries',
        'info@alltoys.uz',
        [company_name.company_email],
        fail_silently=False,
    )