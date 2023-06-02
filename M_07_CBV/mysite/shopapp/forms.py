from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Reviews


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "name",


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = "content",

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ""
