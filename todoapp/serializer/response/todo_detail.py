

class TodoDetailResponseSerializer:
    """
    Converts Todo model object into API response structure
    """

    @staticmethod
    def serialize(obj):
        return {
            "tableName": obj.table_name,
            "tableCode": obj.table_code,
            "tableDescription": obj.table_description,
            "createdDateTime": obj.created_datetime,
            "isActive": obj.is_active,
            "createdBy": obj.created_by,
            "createdBranch": obj.created_branch,
            "createdByCode": obj.created_by_code,
            "createdBranchCode": obj.created_branch_code,
        }
