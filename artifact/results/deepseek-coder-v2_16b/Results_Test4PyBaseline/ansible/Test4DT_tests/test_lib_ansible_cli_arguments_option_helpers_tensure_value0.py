# Module: ansible.cli.arguments.option_helpers
# Import the function using its provided module name.
from ansible.cli.arguments.option_helpers import ensure_value
import pytest

# Test cases for ensure_value function
def test_ensure_value_existing_attribute():
    class Namespace:
        pass
    
    ns = Namespace()
    setattr(ns, 'foo', 42)
    assert ensure_value(ns, 'foo', 42) == 42

def test_ensure_value_non_existing_attribute():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'bar', 100) == 100
    assert hasattr(ns, 'bar')

def test_ensure_value_multiple_attributes():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'foo', 42) == 42
    assert ensure_value(ns, 'baz', 100) == 100
    assert hasattr(ns, 'foo')
    assert hasattr(ns, 'baz')

def test_ensure_value_with_different_values():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'foo', 42) == 42
    assert ensure_value(ns, 'bar', 100) == 100
    assert ensure_value(ns, 'baz', 3.14) == 3.14

def test_ensure_value_with_none_value():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'foo', None) is None
    assert hasattr(ns, 'foo')
