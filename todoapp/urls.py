from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('all/', views.all, name="all"),
    path('all_delete/<int:id>/', views.all_delete, name="all_delete_data"),
    path('add_note/', views.add_note, name="add_note"),
    path('archive/', views.archivepage, name="archivepage"),
    path('delete/<int:id>/', views.delete, name="delete_data"),
    path('deletefromarchive/<int:id>/', views.deletefromarchive, name="deletefromarchive"),
    path('archive/<int:id>/', views.archive, name="archive_data"),
    path('unarchive/<int:id>/', views.unarchive, name="unarchive_data"),
    path('view/<int:id>/', views.view_update, name="view_update"),

    path('login/', views.loginpage, name="loginpage"),
    path('register/', views.registerpage, name="registerpage"),
    path('logout/', views.logoutUser, name="logout"),
    path('copyright/', views.copyright, name="copyright"),
    path('delete_my_account/', views.delete_my_account, name="delete_my_account"),






]
