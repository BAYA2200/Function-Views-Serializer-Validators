from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'cat', views.CategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('cat/', views.CategoryViewSet.as_view({'get': 'list'})),
    # path('cat/create/', views.CategoryViewSet.as_view({'post': 'create'})),
    # path('cat/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve'})),
    path('item/', views.ItemListCreateAPIView.as_view()),
    path('item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
]


