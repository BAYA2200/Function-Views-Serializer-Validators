from django.urls import path

from . import views


urlpatterns = [
    path('cat/', views.CategoryListCreateAPIView.as_view()),
    path('cat/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('item/', views.ItemListCreateAPIView.as_view()),
    path('item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
]