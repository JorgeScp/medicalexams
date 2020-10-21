from django.forms import inlineformset_factory, modelformset_factory

from corecode.models import AcademicSession, AcademicTerm, StudentClass
from .models import Employee_Record, Exams_Record


ExamsFormSet = inlineformset_factory(
    Employee_Record, Exams_Record, fields=('date', 'type_exam', 'comments'), extra=0, can_delete=True
)

Exams_Records = modelformset_factory(Exams_Record, exclude=(), extra=4)

