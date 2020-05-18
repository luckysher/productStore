from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
    path('new-arrival', views.NewArrival.as_view),
]