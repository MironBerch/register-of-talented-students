from django.urls import path
from reporting.views import ContestCreateView, ContestListView, ContestUpdateView, ContestDeleteView, ContestDetailView, ContestExportView


urlpatterns = [
    path('', ContestListView.as_view(), name='list'),
    path('create', ContestCreateView.as_view(), name='create'),
    path('export', ContestExportView.as_view(), name='export'),
    path('update/<int:id>', ContestUpdateView.as_view(), name='update'),
    path('delete/<int:id>', ContestDeleteView.as_view(), name='delete'),
    path('detail/<int:id>', ContestDetailView.as_view(), name='detail'),
]