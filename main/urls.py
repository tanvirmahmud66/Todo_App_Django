from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('is_complete/<str:id>/', views.is_complete, name="is_complete"),
    path('delete_todo/<str:id>/', views.todo_delete, name='delete'),
    path('edit_todo/<str:id>/', views.edit_todo, name='edit'),
]
