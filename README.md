# Todo List

The back-end of a CRUD todo list application made with Django

[Client repository](https://github.com/benfir123/todo-list-client)

## Endpoints

| Description           | Method | URL                          |
| --------------------- | ------ | ---------------------------- |
| Create new todo       | POST   | /api/todos/                  |
| Get list of all todos | GET    | /api/todos/                  |
| Clear all todos       | DELETE | /api/todos/clear/            |
| Reorder todo list     | PATCH  | /api/todos/sort/             |
| Delete single todo    | DELETE | /api/todos/<int:pk>/         |
| Mark todo as done     | PATCH  | /api/todos/<int:pk>/complete |

## Features

- [x] Add new todo
- [x] Delete todo
- [x] Clear todo list
- [x] Mark todo as done
- [x] Show todo list
- [x] Reorder todo list

## Technologies used

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)

## How to use the app

### Step 1

Clone repository

```
git clone https://github.com/benfir123/todolistapi.git
cd todolistapi
```

### Step 2

Install the requirements

```
pip install -r requirements.txt
```

### Step 3

Run app in development mode

```
python manage.py runserver
```

### Step 4

Make test calls to the API by visiting http://localhost:8000/api

## More about the project

This todo list was developed following Test First principles. All the requirements were converted into test cases and code was then refactored to pass said cases. We create a simple todo model with 3 fields: title, is_completed, and position. The position field is a positive integer and is used to manage the order of the todo list items in the database. This is known as an Array structure scheme of sorting a list. This approach has lower insert and update performance than other options but is simple and easy to query.
