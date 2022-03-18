from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('Hours', index),
    path('Category', index),
    path('Usage', index),
    path('Settings', index)
]