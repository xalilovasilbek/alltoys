from django.urls import path
from toys import views

app_name = 'toys'
urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.SignOutView.as_view(), name='logout'),
    path('toys/', views.ToysListView.as_view(), name='toys'),
    path('toys/create', views.ToyCreateView.as_view(), name='toys-create'),
    path('toys/<int:pk>', views.ToyDetailView.as_view(), name='toy_detail'),
    path('users/', views.show_users, name='show_users'),
    path('cabinet/', views.CabinetView, name='cabinet'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('employee/add', views.EmployeeCreateView.as_view(), name='employee-add'),
    path('employee/list/', views.employee_list, name='employee-list'),
    path('employee/list/<int:pk>/edit', views.employee_edit, name='employee-edit')
]
