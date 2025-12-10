from dataclasses import asdict, is_dataclass
from typing import Any

def dataclass_to_primitive(obj: Any) -> Any:
    if is_dataclass(obj):
        return asdict(obj)
    if isinstance(obj, list):
        return [dataclass_to_primitive(x) for x in obj]
    return obj
