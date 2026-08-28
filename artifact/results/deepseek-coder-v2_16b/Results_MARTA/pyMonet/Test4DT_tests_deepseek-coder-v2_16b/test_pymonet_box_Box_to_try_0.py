
import pytest
from pymonet.box import Box

# Test valid input
def test_valid_input():
    box = Box(42)
    try_monad = box.to_try()
    assert try_monad.value == 42
    assert try_monad.is_success is True

# Test with None value
def test_edge_case_none():
    box = Box(None)
    try_monad = box.to_try()
    assert try_monad.value is None
    assert try_monad.is_success is True

# Test with invalid input type
def test_invalid_input():
    box = Box('string')
    try_monad = box.to_try()
    assert try_monad.value == 'string'
    assert try_monad.is_success is True
