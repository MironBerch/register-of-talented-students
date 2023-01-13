from django.urls import path
from reporting.views import ContestCreateView, ReportListView, ContestUpdateView, ContestDeleteView


urlpatterns = [
    path('create', ContestCreateView.as_view(), name='create'),
    path('list', ReportListView.as_view(), name='list'),
    path('update/<int:id>', ContestUpdateView.as_view(), name='update'),
    path('delete/<int:id>', ContestDeleteView.as_view(), name='delete'),
]