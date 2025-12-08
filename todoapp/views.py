from rest_framework import viewsets, status
from rest_framework.response import Response
from todoapp.model.model import Todo
from todoapp.serializer.serializer import TodoSerializer
from rest_framework.decorators import action

class TodoViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Todo.
    URL actions:
      - list: GET /api/todos/
      - create: POST /api/todos/
      - retrieve: GET /api/todos/{id}/
      - update: PUT /api/todos/{id}/
      - partial_update: PATCH /api/todos/{id}/
      - destroy: DELETE /api/todos/{id}/
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

    # Example custom action to toggle completion (optional)
    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        todo = self.get_object()
        todo.is_completed = not todo.is_completed
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)


# Create your views here.
