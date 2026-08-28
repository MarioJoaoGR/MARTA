
import pytest
from unittest.mock import patch
from tornado.escape import to_unicode

def recursive_unicode(obj):
    if isinstance(obj, dict):
        return {recursive_unicode(k): recursive_unicode(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [recursive_unicode(i) for i in obj]
    elif isinstance(obj, tuple):
        return tuple(recursive_unicode(i) for i in obj)
    elif isinstance(obj, bytes):
        return to_unicode(obj)
    else:
        return obj


def test_recursive_unicode_with_nested_structure():
    nested_structure = {
        "list": [b"item1", b"item2"],
        "tuple": (b"element1", b"element2"),
        "dict": {b"key1": b"value1"}
    }
    with patch('tornado.escape.to_unicode', return_value='converted'):
        result = recursive_unicode(nested_structure)
        assert result == {"list": ['item1', 'item2'], "tuple": ('element1', 'element2'), "dict": {'key1': 'value1'}}