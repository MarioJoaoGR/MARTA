
import pytest
from pymonet.validation import Validation

def test_edge_case_none():
    val = Validation.success(None)
    assert val.value is None
    assert len(val.errors) == 0
