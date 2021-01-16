from django.contrib.auth.forms import UserCreationForm

from toys.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2', 'phone'
        ]
