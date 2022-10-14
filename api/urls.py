from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register("todos", views.TodoViewSet, basename="todo")

urlpatterns = [
    path("", views.api_overview, name="api-overview"),
    path("", include(router.urls)),
    path("todos/<str:pk>/", views.todo_delete, name="todo-delete"),
    path("todos/<str:pk>/complete/", views.todo_complete, name="todo-complete"),
    path("todos/sort/", views.todo_sort, name="todo-sort"),
]
