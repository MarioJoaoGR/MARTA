
import pytest
from dataclasses_json.utils import _is_mapping, _get_type_origin
from typing import Mapping

def test_valid_case_custom_mapping():
    from collections import defaultdict
    
    class MyDict(dict): pass
    
    assert _is_mapping(defaultdict) is True
    assert _is_mapping(MyDict) is True
    assert _is_mapping(type) is False  # Ensure it handles built-in types correctly
