
import pytest
from typing import Dict, DefaultDict, Mapping
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe

# Test cases for _is_mapping function
def test_is_mapping_builtin():
    assert _is_mapping(dict) == True
    assert _is_mapping(DefaultDict[str, int]) == True

def test_is_mapping_custom():
    class MyCustomMapping: pass