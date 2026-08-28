# Module: pymonet.maybe
import pytest
from pymonet.maybe import Maybe

# Test cases for the Maybe class and its get_or_else method
def test_get_or_else_with_value():
    maybe = Maybe(value=42, is_nothing=False)
    assert maybe.get_or_else(default_value=0) == 42

def test_get_or_else_with_nothing():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.get_or_else(default_value=0) == 0

def test_get_or_else_with_custom_default():
    maybe = Maybe(value=42, is_nothing=False)
    assert maybe.get_or_else(default_value="default") == 42

def test_get_or_else_with_none_default():
    maybe = Maybe(value=None, is_nothing=True)
    assert maybe.get_or_else(default_value=None) is None
