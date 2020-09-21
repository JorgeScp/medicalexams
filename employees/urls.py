from django.urls import path

from .views import student_list, StudentDeleteView, StudentDetailView, StudentUpdateView, StudentCreateView, StudentBulkUploadView,downloadcsv

urlpatterns = [
  path('list', student_list, name='employee-list'),
  path('<int:pk>/', StudentDetailView.as_view(), name='employee-detail'),
  path('create/', StudentCreateView.as_view(), name='employee-create'),
  path('<int:pk>/update/', StudentUpdateView.as_view(), name='employee-update'),
  path('delete/<int:pk>/', StudentDeleteView.as_view(), name='employee-delete'),

  path('upload/', StudentBulkUploadView.as_view(), name='employee-upload'),
  path('downloadcsv/', downloadcsv, name='download-csv'),

]
