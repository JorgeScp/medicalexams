from django.contrib import admin
from .models import Exams_Record, Employee_Record
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

# class ExamsResource(resources.ModelResource):

#     class Meta:
#         model = Exams_Record

@admin.register(Exams_Record)
class ExamsAdmin(ImportExportModelAdmin):
    author = Field(
        column_name='author',
        attribute='author',
        widget=ForeignKeyWidget(Employee_Record, 'name'))

    class Meta:
        model = Exams_Record
        fields = ('author',)

# admin.site.register(Exams_Record)
admin.site.register(Employee_Record)
# Register your models here.
