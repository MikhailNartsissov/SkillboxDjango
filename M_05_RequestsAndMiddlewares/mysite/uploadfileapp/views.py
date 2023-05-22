
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    """

    :param request:
    :return:
    """
    if request.method == 'POST' and request.FILES.get('file_to_upload'):
        if request.FILES['file_to_upload'].size < 1048576:
            file_to_upload = request.FILES['file_to_upload']
            file_system_storage = FileSystemStorage()
            file_name = file_system_storage.save(file_to_upload.name, file_to_upload)
        else:
            return render(request, "uploadfileapp/upload-denial.html")
    return render(request, "uploadfileapp/file-upload.html")
