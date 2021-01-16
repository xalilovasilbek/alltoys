from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, resolve_url
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView

from toys.forms.employee_add import EmployeeModelForm
from toys.forms.sign_up import SignUpForm
from toys.forms.toy import ToyModelForm
from toys.forms.user import LoginForm
from toys.models import Toy, User, Employee
from django.shortcuts import render
from django.contrib.auth import login, authenticate


class DashboardView(TemplateView):
    template_name = 'toys/dashboard.html'
    extra_context = {'welcome_text': 'Welcome to AllToys!'}


# Bu method orqali extra_contextni o'zgartirish mumkin
'''    def get_context_data(self, **kwargs):          
        super().get_context_data(**kwargs)
        self.extra_context['welcome_text'] = 'AllToysga xush kelibsiz'
        if self.extra_context is not None:
            self.extra_context.update(self.extra_context)
            return self.extra_context'''


# class DashboardView(View):
#     def get(self, request):
#         return render(request, template_name='toys/dashboard.html', context={'welcome_text': 'Welcome to AllToys!'})


class ToysListView(ListView):
    model = Toy
    template_name = 'toys/toys.html'
    queryset = Toy.objects.filter()

    def get_queryset(self):
        toys = Toy.objects.filter(created_at__year=timezone.now().year)
        return toys


class ToyDetailView(DetailView):
    model = Toy
    template_name = 'toys/toy_detail.html'


class ToyCreateView(View):
    template_name = 'toys/toy.html'

    def get(self, request):
        if not request.user.is_authenticated:
            url = resolve_url('toys:login') + '?next=' + request.get_full_path()
            return redirect(url)
        form = ToyModelForm()
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = ToyModelForm(data=request.POST)
        if form.is_valid():
            toy = form.save()
            return redirect(to='toys:toy_detail', pk=toy.id)
        context = {'form': form}
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'toys/login.html'

    def get(self, request):
        # if request.user.is_authenticated:
        #     return redirect('toys:dashboard')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            redirect_to = request.GET.get('next')
            if not redirect_to:
                redirect_to = 'toys:cabinet'
            return redirect(to=redirect_to)
        context = {'form': form}
        return render(request, self.template_name, context)


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('toys:login')
#     else:
#         form = SignUpForm()
#     return render(request, 'toys/signup.html', {'form': form})


class SignUp(TemplateView):
    template_name = 'toys/signup.html'

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'toys/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('toys:login')
        return render(request, 'toys/signup.html', {'form': form})


class SignOutView(LogoutView):
    pass


def show_users(request):
    users = User.objects.all()
    return render(request, 'toys/show_users.html', context={'users_list': users})


def CabinetView(request):
    username = request.user
    return render(request, 'toys/cabinet.html', context={'username': username})


class EmployeeCreateView(View):
    template_name = 'toys/employee.html'

    def get(self, request):
        if not request.user.is_authenticated:
            url = resolve_url('toys:login') + '?next=' + request.get_full_path()
            return redirect(url)
        form = EmployeeModelForm()
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = EmployeeModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='toys:employee-list')
        context = {'form': form}
        return render(request, self.template_name, context)


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'toys/employee_list.html', context)


def employee_edit(request, pk=None):
    instance = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('toys:employee-list')
    else:
        form = EmployeeModelForm(instance=instance)
    return render(request, 'toys/employee_edit.html', {'form': form})
