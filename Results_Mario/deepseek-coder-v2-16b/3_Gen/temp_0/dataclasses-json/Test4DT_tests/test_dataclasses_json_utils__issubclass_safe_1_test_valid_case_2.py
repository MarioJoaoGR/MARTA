
import pytest
from dataclasses_json.utils import _issubclass_safe, _is_new_type, _is_new_type_subclass_safe

def test_valid_case_2():
    class C: pass
    assert not _issubclass_safe(C, int), "Expected False because C does not subclass int"
