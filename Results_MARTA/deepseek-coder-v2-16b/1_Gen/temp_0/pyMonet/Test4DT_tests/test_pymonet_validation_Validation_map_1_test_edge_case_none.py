
import pytest
from pymonet.validation import Validation

def test_edge_case_none():
    val = Validation(None, ['Initial error'])
    assert len(val.errors) == 1
    assert val.value is None
