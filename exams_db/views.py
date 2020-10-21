from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from employees.models import Student
from .models import Employee_Record, Exams_Record
from .forms import ExamsFormSet, Exams_Records

class EmployeeRListView(LoginRequiredMixin, ListView):
  model = Employee_Record


class EmployeeRCreateView(LoginRequiredMixin, CreateView):
    model = Employee_Record
    fields = '__all__'
    success_url = '/exams_db/list/'

    def get_context_data(self, **kwargs):
        context = super(EmployeeRCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['items'] = ExamsFormSet(
                self.request.POST, prefix='exams_set')
        else:
            context['items'] = ExamsFormSet(prefix='exams_set')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['items']
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class EmployeeRDetailView(LoginRequiredMixin, DetailView):
    model = Employee_Record
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(EmployeeRDetailView, self).get_context_data(**kwargs)
        context['exams_records'] = Exams_Record.objects.filter(employee_record=self.object)
        return context

class ExamsDetailView(LoginRequiredMixin, DetailView):
    model = Exams_Record
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ExamsDetailView, self).get_context_data(**kwargs)
        exams_record = Exams_Record.objects.get(pk=self.kwargs['pk'])
        context['exams_records'] = exams_record
        
        return context

class EmployeeRUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee_Record
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(EmployeeRUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
          context['exams_records'] = ExamsFormset(
              self.request.POST, instance=self.object)

        else:
          context['exams_records'] = ExamsFormset(instance=self.object)
        return context

    def form_valid(self, form):
      context = self.get_context_data()
      formset = context['exams_records']
      if form.is_valid() and formset.is_valid() and itemsformset.is_valid():
        form.save()
        formset.save()
      return super().form_valid(form)



class EmployeeRDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee_Record
    success_url = reverse_lazy('employeer-list')


class ExamsRCreateView(LoginRequiredMixin, CreateView):
    model = Exams_Record
    fields = '__all__'
    success_url = reverse_lazy('employeer-list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        employee_record = Employee_Record.objects.get(pk=self.request.GET['employee_record'])
        obj.employee_record = employee_record
        obj.save()
        return redirect('employeer-list')

    def get_context_data(self, **kwargs):
        context = super(ExamsRCreateView, self).get_context_data(**kwargs)
        employee_record = Employee_Record.objects.get(pk=self.request.GET['employee_record'])
        context['employee_record'] = employee_record
        return context


class ExamsRUpdateView(LoginRequiredMixin, UpdateView):
    model = Exams_Record
    fields = ['date', 'type_exam', 'comments']
    success_url = reverse_lazy('employeer-list')


class ExamsRDeleteView(LoginRequiredMixin, DeleteView):
    model = Exams_Record
    success_url = reverse_lazy('employeer-list')

@login_required
def bulk_invoice(request):
    return render(request, 'finance/bulk_invoice.html')
