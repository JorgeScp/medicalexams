from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Exams

@login_required
def exams_list(request):
  exams = Exams.objects.all()
  return render(request, 'exams/exams_list.html', {"exams":exams})


class StaffListView(ListView):
    model = Exams
    

class StaffDetailView(DetailView):
    model = Exams
    template_name = "exams/exams_detail.html"


class StaffCreateView(SuccessMessageMixin, CreateView):
    model = Exams
    fields = '__all__'
    success_message = 'New staff successfully added'

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffCreateView, self).get_form()
        # form.fields['date_of_birth'].widget = widgets.DateInput(
        #     attrs={'type': 'date'})
        # form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
        #                                                             'type': 'date'})
        # form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        # form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form


class StaffUpdateView(SuccessMessageMixin, UpdateView):
    model = Exams
    fields = '__all__'
    success_message = "Record successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(StaffUpdateView, self).get_form()
        # form.fields['date_of_birth'].widget = widgets.DateInput(
        #     attrs={'type': 'date'})
        # form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
        #                                                             'type': 'date'})
        # form.fields['address'].widget = widgets.Textarea(attrs={'rows': 1})
        # form.fields['others'].widget = widgets.Textarea(attrs={'rows': 1})
        return form

class StaffDeleteView(DeleteView):
  model = Exams
  success_url = reverse_lazy('exams-list')
