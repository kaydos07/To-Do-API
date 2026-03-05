from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.get_tasks, name='task-list'),
    path('create/', views.create_task, name='task-create'),
    path('view/<int:id>/', views.get_task_detail, name='task-detail'),
    path('update/<int:id>/', views.update_task, name='task-update'),
    path('delete/<int:id>/', views.delete_task, name='task-delete')
]