
import pytest
from dataclasses_json.utils import _is_new_type_subclass_safe

def test_error_case_invalid_input():
    class C: pass
    
    # Test with an invalid type for classinfo
    assert not _is_new_type_subclass_safe(C, int)
