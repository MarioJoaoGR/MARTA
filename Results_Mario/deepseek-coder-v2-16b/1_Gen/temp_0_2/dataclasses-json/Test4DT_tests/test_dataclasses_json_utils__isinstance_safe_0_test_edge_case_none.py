
import pytest
from dataclasses_json.utils import _isinstance_safe

def test_edge_case_none():
    # Test when None is passed as the object
    assert not _isinstance_safe(None, int)  # Should return False since None cannot be an instance of any type including int
    assert not _isinstance_safe(None, (int, float))  # Should return False for the same reason
