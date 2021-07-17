
from django.urls import path

from .views import create, detail, delete
urlpatterns = [
 path('create', create, name="create"),
 path('<int:id>', detail, name="detail"),
 path('delete/<int:id>', delete, name="delete"),
]