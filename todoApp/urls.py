from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:pk>', views.task, name='task'),
    path('create-task', views.create_task, name='create-task'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name = 'register'),
    path('my-login', views.my_login, name = 'my-login'),
    path('my-logout', views.my_logout, name = 'my-logout'),
]
