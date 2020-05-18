from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.ProductListCreateView.as_view() ),
    path('api/news/', views.NewsListCreateView.as_view() ),
]