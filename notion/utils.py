from typing import Any, Dict


def composed_dict(base: Dict[Any, Any], *args: str) -> Dict[Any, Any]:
    """Returned a pair of key-value"""
    for key in args:
        if key in base:
            return {key: base}


def remove_key(base: Dict[Any, Any]) -> Dict[Any, Any]:
    """Remove key from dictionary object"""
    for key, value in dict.items(base):
        if value != object():
            return {key: value}
