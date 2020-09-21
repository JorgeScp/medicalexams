from django.urls import path

from .views import StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDetailView, StaffDeleteView, exams_list

urlpatterns = [
  #path('list/', exams_list, name='exams-list'),
  path('list/', StaffListView.as_view(), name='exams-list'),
  path('<int:pk>/', StaffDetailView.as_view(), name='exams-detail'),
  path('create/', StaffCreateView.as_view(), name='exams-create'),
  path('<int:pk>/update/', StaffUpdateView.as_view(), name='exams-update'),
  path('<int:pk>/delete/', StaffDeleteView.as_view(), name='exams-delete'),
]
