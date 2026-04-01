
import pytest
from dataclasses_json.utils import _is_mapping, _issubclass_safe, _get_type_origin
from typing import Mapping
from collections import defaultdict

def test_valid_case_dict():
    class MyDict(dict): pass
    
    assert _is_mapping(defaultdict) is True
    assert _is_mapping(MyDict) is True
    assert _is_mapping(int) is False  # Example of a non-mapping type
