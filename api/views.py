from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.


@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "Create todo (POST)": "/todos/",
        "Get list of todos (GET)": "/todos/",
        "Clear todo list (DELETE)": "/todos/clear/",
        "Reorder todo list (PATCH)": "/todos/sort/",
        "Delete todo (DELETE)": "/todos/<int:pk>/",
        "Mark as done (PATCH)": "/todos/<int:pk>/complete/",
    }
    return Response(api_urls)


class TodoViewSet(ViewSet):
    def create(self, request):
        for x in range(Todo.objects.count() - 1, -1, -1):
            todo = Todo.objects.get(position=x)
            todo.position += 1
            todo.save(update_fields=["position"])

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        todos = Todo.objects.all().order_by("position")
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        todo = Todo.objects.get(id=pk)
        todo.delete()

        for x in range(Todo.objects.count() - todo.position):
            other_todo = Todo.objects.get(position=x + todo.position + 1)
            other_todo.position -= 1
            other_todo.save(update_fields=["position"])

        return Response("Todo successfully deleted!")

    @action(detail=False, methods=["DELETE"], name="todo-clear")
    def clear(self, request):
        Todo.objects.all().delete()
        return Response(
            "Todos cleared successfully!", status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=False, methods=["PATCH"], name="todo-sort")
    def sort(self, request):
        source, destination = request.data.values()

        if source != destination:
            source_pk = Todo.objects.get(position=source).id

            if source > destination:
                for x in range(source - destination, destination - 1, -1):
                    todo = Todo.objects.get(position=x)
                    todo.position += 1
                    todo.save(update_fields=["position"])

            if source < destination:
                for x in range(destination - source, destination + 1):
                    todo = Todo.objects.get(position=x)
                    todo.position -= 1
                    todo.save(update_fields=["position"])

            source_todo = Todo.objects.get(id=source_pk)
            source_todo.position = destination
            source_todo.save(update_fields=["position"])

        return Response("Todo successfully sorted!")

    @action(detail=True, methods=["PATCH"], name="todo-complete")
    def complete(self, request, pk=None):
        todo = Todo.objects.get(id=pk)
        if todo.is_completed == True:
            todo.is_completed = False
        else:
            todo.is_completed = True
        todo.save(update_fields=["is_completed"])

        return Response(
            "Todo successfully (un)completed!",
            status=status.HTTP_204_NO_CONTENT,
        )
