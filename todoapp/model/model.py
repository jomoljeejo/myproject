# todoapp/model/model.py
from typing import Any, Dict, List, Optional

from django.db import models

# import the dataclass DTO that holds Meta.table_name
from todoapp.dataclass.request.create import TodoCreateDTO


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # use the dataclass Meta.table_name as single source of truth
        db_table = TodoCreateDTO.Meta.table_name

    def __str__(self):
        return self.title

    # ---------------- DB helper methods (used by views) ----------------

    @classmethod
    def create_todo(
        cls,
        *,
        title: str,
        description: Optional[str] = None,
        is_done: bool = False,
        **kwargs: Any,
    ) -> "Todo":
        """
        Create and return a Todo instance.
        Extra kwargs accepted for forward-compatibility (e.g. organisation_id) but ignored.
        """
        return cls.objects.create(
            title=title,
            description=description or "",
            is_done=is_done,
        )

    @classmethod
    def update_todo(
        cls,
        *,
        id: int,
        fields: Dict[str, Any],
    ) -> "Todo":
        """
        Update the Todo identified by `id` with `fields` dict and return the updated instance.
        Raises Todo.DoesNotExist if no matching row.
        """
        qs = cls.objects.filter(pk=id)
        updated_count = qs.update(**fields)
        if updated_count == 0:
            raise cls.DoesNotExist(f"Todo with id {id} not found.")
        return cls.objects.get(pk=id)

    @classmethod
    def get_todo(cls, *, id: int) -> "Todo":
        """
        Return a Todo instance by primary key. Raises DoesNotExist if none.
        """
        return cls.objects.get(pk=id)

    @classmethod
    def list_todos(cls, *, filters: Optional[Dict[str, Any]] = None) -> List["Todo"]:
        """
        Return a list of todos. Optional filters can be passed as a dict.
        """
        qs = cls.objects.all().order_by("-created_at")
        if filters:
            qs = qs.filter(**filters)
        return list(qs)

    @classmethod
    def delete_many_todos(cls, *, ids: List[int]) -> None:
        """
        Delete todos whose primary keys are in `ids`.
        Returns the (num_deleted, detail) tuple from QuerySet.delete() if you want it;
        here we return None for simplicity.
        """
        cls.objects.filter(pk__in=ids).delete()
