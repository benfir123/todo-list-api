from turtle import position, title
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Todo

# Create your tests here.


class TodoTests(APITestCase):
    def setUp(self):
        data = {
            0: "Have meeting",
            1: "Meet Emma",
            2: "Go to market",
            3: "Do laundry",
            4: "Buy groceries",
        }
        for position, title in data.items():
            Todo.objects.create(position=position, title=title)

    def test_create_todo(self):
        """
        Ensure we can create a new todo object.
        """
        url = reverse("todo-list")
        data = {"title": "Research term paper"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 6)
        self.assertEqual(
            response.data,
            {
                "id": 6,
                "title": "Research term paper",
                "position": 0,
                "is_completed": False,
            },
        )
        self.assertEqual(Todo.objects.get(position=1).title, "Have meeting")

    def test_retrieve_todos(self):
        """
        Ensure we can retrive all todo objects.
        """
        url = reverse("todo-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_clear_todos(self):
        """
        Ensure we can clear all todo objects.
        """
        url = reverse("todo-list")
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)

    def test_sort_todos(self):
        """
        Ensure we can sort all todo objects.
        """
        url = reverse("todo-sort")
        data = {"source": 3, "destination": 1}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(
            response.data,
            {
                {"position": 1, "title": "Do laundry"},
                {"position": 2, "title": "Meet Emma"},
                {"position": 3, "title": "Go to market"},
            },
        )
        self.assertEqual(Todo.objects.get(position=1).title, "Do laundry")
        self.assertEqual(Todo.objects.get(position=2).title, "Meet Emma")
        self.assertEqual(Todo.objects.get(position=3).title, "Go to market")

    def test_delete_todo(self):
        """
        Ensure we can delete a single todo.
        """
        url = reverse("todo-delete", args=[4])
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.get(id=4), None)
        self.assertEqual(Todo.objects.get(id=5).position, 3)
        self.assertEqual(
            response.data,
            {"id": 4, "position": 3, "is_completed": False, "title": "Do laundry"},
        )

    def test_complete_todo(self):
        """
        Ensure we can mark a single todo complete.
        """
        url = reverse("todo-complete", args=[4])
        response = self.client.patch(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.get(id=4).is_completed, True)
