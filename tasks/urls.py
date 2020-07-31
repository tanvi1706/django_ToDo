from . import views
from django.urls import path
urlpatterns = [
		path('', views.index, name="index"),
		path('update_task/<str:pk>/', views.updateTask, name="upd"),
		path('delete/<str:pk>', views.deleteTask, name="delete"),

]