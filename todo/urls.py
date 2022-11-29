
from django.urls import path, include
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginViews, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('main/', views.main),

    path('login/', CustomLoginViews.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('', TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='taskCreate'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='taskUpdate'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='taskDelete'),

]
