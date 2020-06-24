from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('update_item/<str:pk>/', views.update_item, name="update_item"),
    path('delete/<str:pk>/', views.delete, name="delete")
]