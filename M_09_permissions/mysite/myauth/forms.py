from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name', 'agreement_accepted']
        exclude = ["username"]


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'agreement_accepted', 'is_active', 'biography']

