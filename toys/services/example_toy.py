from django.db import transaction
from django.db.models import F

from toys.models import Company, Employee


# def rename_company_name():
#     with transaction.atomic():
#         old_name = Company.objects.all()[0]
#         old_name.company_name = 'ECMA'
#         new_name = old_name.save()
#         try:
#             with transaction.atomic():
#                 Employee.objects.update(salary=F('salary') * 1.1)
#                 raise Exception('Uzr!')
#         except Exception:
#             pass
