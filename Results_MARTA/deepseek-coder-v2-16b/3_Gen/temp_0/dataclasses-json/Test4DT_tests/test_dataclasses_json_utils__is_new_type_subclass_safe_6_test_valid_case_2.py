
import pytest
from dataclasses_json.utils import _is_new_type_subclass_safe

def test_valid_case_2():
    class C: pass
    assert not _is_new_type_subclass_safe(C, int)
