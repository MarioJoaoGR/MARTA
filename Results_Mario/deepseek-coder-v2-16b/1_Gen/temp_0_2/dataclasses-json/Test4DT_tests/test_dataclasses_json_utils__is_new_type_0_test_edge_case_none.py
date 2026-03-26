
import pytest
import inspect
from dataclasses_json.utils import _is_new_type

def test_edge_case_none():
    """
    Test edge case with None input
    """
    assert not _is_new_type(None), "Expected False for None input, but got True"
