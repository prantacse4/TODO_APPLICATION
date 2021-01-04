from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_note/', views.add_note, name="add_note"),
    path('delete/<int:id>/', views.delete, name="delete_data"),
    path('archive/<int:id>/', views.archive, name="archive_data"),
]
