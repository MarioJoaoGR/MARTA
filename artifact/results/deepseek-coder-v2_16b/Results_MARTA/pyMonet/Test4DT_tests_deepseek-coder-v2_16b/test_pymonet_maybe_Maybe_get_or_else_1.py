
import pytest
from pymonet.maybe import Maybe

# Scenario 1: Test get_or_else method with a non-null value
def test_get_or_else_with_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert maybe_some.get_or_else('default') == 42

# Scenario 2: Test get_or_else method with a null value
def test_get_or_else_with_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.get_or_else('default') == 'default'

# Scenario 3: Test get_or_else method with a default value
def test_get_or_else_with_default():
    default_value = 'Default Value'
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.get_or_else(default_value) == default_value
