from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from django.db.models.options import Options
from csv import writer


class ExportAsCSVMixin:
    """
    Class-mixin for saving data into .csv file
    """
    def export_csv(self, request: HttpRequest, queryset: QuerySet) -> HttpResponse:
        """
        Saves data into .csv file and returns HttpResponse
        :param request:
        :param queryset:
        :return:
        """
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={meta}-export.csv"

        csv_writer = writer(response)
        csv_writer.writerow(field_names)

        for obj in queryset:
            csv_writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_csv.short_description = "Export selected as .csv"
