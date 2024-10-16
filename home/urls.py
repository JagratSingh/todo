from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.TaskList, name="task-list"),
    path('task-detail/<str:pk>/', views.TaskDetail, name="task-Detail"),
    path('update-task/<str:pk>/', views.UpdateTask, name="update-task"),
    path('delete-task/<str:pk>/', views.DeleteTask, name="delete-task"),
    path('create-task/', views.CreateTask, name="Create-task"),
]
