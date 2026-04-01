
import pytest
from typing import Mapping
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe

def test_invalid_input():
    class NotAMapping: pass
    
    assert not _is_mapping(NotAMapping)
