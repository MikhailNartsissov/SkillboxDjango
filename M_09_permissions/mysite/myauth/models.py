from django.db.models import Model, OneToOneField, BooleanField, TextField, CASCADE
from django.contrib.auth.models import User


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField(max_length=500, blank=True)
    agreement_accepted = BooleanField(default=False)
