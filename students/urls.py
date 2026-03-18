from django.urls import path
from . import views

urlpatterns = [
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('classrooms/<int:pk>/', views.classroom_detail, name='classroom_detail'),
]