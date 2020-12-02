import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Employee, StudentBulkUpload
from finance.models import Invoice

@login_required
def student_list(request):
  students = Employee.objects.all()
  return render(request, 'employees/employee_list.html', {"students":students})


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        # context['payments'] = Invoice.objects.filter(student=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Employee
    fields = '__all__'
    success_message = "Nuevo colaborador agregado."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StudentCreateView, self).get_form()
        # form.fields['date_of_birth'].widget = widgets.DateInput(
        #     attrs={'type': 'date'})
        # form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        # form.fields['others'].widget = widgets.Textarea(attrs={'rows': 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employee
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StudentUpdateView, self).get_form()
        # form.fields['date_of_birth'].widget = widgets.DateInput(
        #     attrs={'type': 'date'})
        # form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
        #                                                             'type': 'date'})
        # form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        # form.fields['others'].widget = widgets.Textarea(attrs={'rows': 2})
       # form.fields['passport'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = 'students/employee_upload.html'
    fields = ['csv_file']
    success_url = '/employee/list'
    success_message = 'Successfully uploaded students'

@login_required
def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_template.csv"'

    writer = csv.writer(response)
    writer.writerow(['registration_number', 'surname',
                     'firstname', 'other_names', 'gender', 'parent_number', 'address', 'current_class'])

    return response
