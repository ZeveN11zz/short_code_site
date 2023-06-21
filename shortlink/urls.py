from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('result/<str:pk>/', views.result_page, name='result_page'),
    path('<str:pk>/', views.rdir_link, name='rdir_link'),
]