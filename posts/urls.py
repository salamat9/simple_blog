from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('create/', views.create_post, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.edit_post, name='post_edit'),
    path('<int:pk>/delete/', views.delete_post, name='post_delete'),
    path('', views.post_list, name='post_list')
]