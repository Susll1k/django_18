from django.urls import path
from django.urls import include
from app.views import add_task, task_list, manage_tasks

urlpatterns = [
    path('', task_list, name='task_list'),
    path('manage/', manage_tasks, name='manage_tasks'),
    path('add_task/', add_task, name='add_task'),
    path('captcha/', include('captcha.urls')),
]
