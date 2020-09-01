from django.urls import path
from .views import Flattener


urlpatterns = [
    path('flattener/', Flattener.as_view()),
]
