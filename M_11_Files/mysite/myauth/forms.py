from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User


class AvatarForm(ModelForm):
    class Meta:
        model = Profile
        fields = 'avatar',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].label = "Загрузить аватар"