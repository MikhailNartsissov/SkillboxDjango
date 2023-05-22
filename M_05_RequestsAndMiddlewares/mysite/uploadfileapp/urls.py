from django.urls import path
from .views import handle_file_upload

app_name = "uploadfileapp"
urlpatterns = [
    path("", handle_file_upload, name="file-upload"),
]
