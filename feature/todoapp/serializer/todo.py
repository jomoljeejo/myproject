from rest_framework import serializers
from feature.todoapp.model.model import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
