from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

# register the ViewSet route - this creates urls and path names based on
# predefined function names such as create, list, and destroy
router.register("todos", views.TodoViewSet, basename="todo")

urlpatterns = [
    path("", views.api_overview, name="api-overview"),
    path("", include(router.urls)),
]
