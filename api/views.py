from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import TodoSerializer

from .models import Todo

# Create your views here.


@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "Create todo": "/todos/",
        "Get list of todos": "/todos/",
        "Clear todo list": "/todos/",
        "Reorder todo list": "/todos/sort/",
        "Delete todo": "/todos/<str:pk>/",
        "Mark as done": "/todos/<str:pk>/complete/",
    }
    return Response(api_urls)


class TodoViewSet(ViewSet):
    def create(self, request):
        todos = ""
        return Response(todos)

    def list(self, request):
        todos = ""
        return Response(todos)

    def destroy(self, request, pk=None):
        todos = ""
        return Response(todos)


@api_view(["PATCH"])
def todo_sort(request):
    todos = ""
    return Response(todos)


@api_view(["DELETE"])
def todo_delete(request):
    todos = ""
    return Response(todos)


@api_view(["PATCH"])
def todo_complete(request, pk):
    todos = ""
    return Response(todos)
