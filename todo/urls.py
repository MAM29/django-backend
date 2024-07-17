from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list),
    path('delete_task/<int:pk>', views.delete_task)
]
