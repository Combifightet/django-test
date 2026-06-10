from django.urls import path
from . import views

urlpatterns = [
    path("tables/<int:table_id>/rows/", views.view_rows),
]
