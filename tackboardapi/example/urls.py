from django.urls import path
from .views import TestEndpoint

urlpatterns = [
    path('api/hello', TestEndpoint.as_view()),
]