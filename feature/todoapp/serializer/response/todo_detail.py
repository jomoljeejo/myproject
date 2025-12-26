class TodoDetailResponseSerializer:

    @staticmethod
    def serialize(obj):
        return {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description,
            "is_done": obj.is_done,
            "created_at": obj.created_at,
            "updated_at": obj.updated_at,
        }
