from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/all/', views.todo_list, name='todo_list'),
    path('/<str:id>/', views.todo_detail, name='todo_detail'),
    path('/', views.todo_create, name='todo_create'),
    path('/<str:id>', views.todo_update, name='todo_update'),
]