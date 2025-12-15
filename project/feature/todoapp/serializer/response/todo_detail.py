class TodoDetailResponseSerializer:
    """
    Converts Todo model object into standard API response structure
    (Derived from existing Todo fields)
    """

    @staticmethod
    def serialize(obj):
        return {
            # Derived / mapped fields
            "tableName": obj.title,                         # from title
            "tableCode": f"TODO-{obj.id}",                  # derived
            "tableDescription": obj.description,            # from description

            "createdDateTime": obj.created_at,              # from created_at
            "isActive": not obj.is_done,                    # logical mapping

            # Metadata (not in model → derived / static / null)
            "createdBy": "System",                           # default
            "createdBranch": None,
            "createdByCode": "SYS",
            "createdBranchCode": None,
        }
