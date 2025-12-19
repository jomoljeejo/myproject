from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "todo"

    def __str__(self):
        return self.title


    @staticmethod
    def create(title: str, description: str = "", is_done: bool = False):
        return Todo.objects.create(
            title=title,
            description=description,
            is_done=is_done
        )


    @staticmethod
    def get_all():
        return Todo.objects.all().order_by("id")


    @staticmethod
    def get_one(todo_id: int):
        return Todo.objects.filter(id=todo_id).first()


    @staticmethod
    def update(todo_id: int, **data):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return None

        for field, value in data.items():
            setattr(todo, field, value)

        todo.save()
        return todo


    @staticmethod
    def delete_one(todo_id: int):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return False

        todo.delete()
        return True
