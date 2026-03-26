
import pytest
from pymonet.validation import Validation

def test_edge_case_none():
    val = Validation(None, ['Initial error'])
    assert val.value is None
    assert len(val.errors) == 1
    assert val.errors[0] == 'Initial error'
