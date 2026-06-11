from django.urls import path
from . import views

urlpatterns = [
    path("tables/<int:view_id>/rows/", views.view_rows),
]
