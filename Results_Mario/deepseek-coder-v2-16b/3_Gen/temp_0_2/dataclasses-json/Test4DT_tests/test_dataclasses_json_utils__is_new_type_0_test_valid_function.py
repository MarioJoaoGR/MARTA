
import pytest
from unittest.mock import Mock
import inspect
from dataclasses_json.utils import _is_new_type

@pytest.fixture
def is_new_type():
    return _is_new_type

@pytest.mark.parametrize("type_, expected", [
    (Mock(spec=lambda: None), False),  # Not a function or class
    (Mock(spec=lambda: None, __supertype__=None), True),  # Class without __supertype__
    (Mock(spec=lambda: None, __supertype__="NewStyleClass"), True),  # Class with __supertype__
])
def test_valid_function(is_new_type, type_, expected):
    assert is_new_type(type_) == expected
