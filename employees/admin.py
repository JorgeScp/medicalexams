from django.contrib import admin
from .models import Employee
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):

    class Meta:
        model = Employee