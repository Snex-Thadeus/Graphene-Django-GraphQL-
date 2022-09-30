from rest_framework import viewsets

from app.models import Todo
from app.rest.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer