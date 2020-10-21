from django.urls import path

from .views import EmployeeRCreateView, EmployeeRListView, ExamsDetailView, EmployeeRDeleteView, EmployeeRDetailView,EmployeeRUpdateView,ExamsRCreateView, ExamsRUpdateView, bulk_invoice

urlpatterns = [
    path('list/', EmployeeRListView.as_view(), name='employeer-list'),
    path('create/', EmployeeRCreateView.as_view(), name='employeer-create'),
    path('<int:pk>/detail/', EmployeeRDetailView.as_view(), name='employeer-detail'),
    path('<int:pk>/detail_exam/', ExamsDetailView.as_view(), name='examsr-detail'),
    path('<int:pk>/update/', EmployeeRUpdateView.as_view(), name='employeer-update'),
    path('<int:pk>/delete/', EmployeeRDeleteView.as_view(), name='employeer-delete'),
    path('examsr/create', ExamsRCreateView.as_view(), name='examsr-create'),
    path('examsr/<int:pk>/update/', ExamsRUpdateView.as_view(), name='examsr-update'),

    path('bulk-invoice/',  bulk_invoice, name='bulk-invoice'),
]
