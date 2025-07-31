from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('toggle/<int:pk>/', views.task_toggle, name='task_toggle'),
    path('bulk-action/', views.task_bulk_action, name='task_bulk_action'),
    path('export/', views.export_tasks_csv, name='export_tasks_csv'),
    path('statistics/', views.task_statistics, name='task_statistics'),
    path('search/', views.quick_search, name='quick_search'),
] 