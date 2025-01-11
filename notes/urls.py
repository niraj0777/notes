from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),           # List notes
    path('create/', views.note_create, name='note_create'), # Create note
    path('<int:pk>/', views.note_detail, name='note_detail'), # Note details
    path('<int:pk>/delete/', views.note_delete, name='note_delete'), # Delete note
]
