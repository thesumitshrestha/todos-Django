from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('deleteTask/<str:pk>/', views.deleteTask, name="delete_my_task")
]
