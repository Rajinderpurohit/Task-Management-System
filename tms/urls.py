from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('register/', views.sign_page, name='sign'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),
    path('delete/', views.del_task, name='del_task'),
]