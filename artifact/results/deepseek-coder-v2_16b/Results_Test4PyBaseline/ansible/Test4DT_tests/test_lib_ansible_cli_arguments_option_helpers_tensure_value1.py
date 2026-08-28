
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
    # Ensure the attribute remains unchanged if it already exists
    assert getattr(ns, 'foo') == 42

def test_ensure_value_non_existing_attribute():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'bar', 100) == 100
    # Ensure the new attribute has been added
    assert hasattr(ns, 'bar')
    assert getattr(ns, 'bar') == 100

def test_ensure_value_multiple_attributes():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'foo', 42) == 42
    assert ensure_value(ns, 'baz', 100) == 100
    # Ensure both attributes have been added and are unchanged
    assert hasattr(ns, 'foo')
    assert getattr(ns, 'foo') == 42
    assert hasattr(ns, 'baz')
    assert getattr(ns, 'baz') == 100

def test_ensure_value_with_different_values():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'foo', 42) == 42
    assert ensure_value(ns, 'bar', 100) == 100
    assert ensure_value(ns, 'baz', 3.14) == 3.14
    # Ensure all attributes have been added and are unchanged
    assert hasattr(ns, 'foo')
    assert getattr(ns, 'foo') == 42
    assert hasattr(ns, 'bar')
    assert getattr(ns, 'bar') == 100
    assert hasattr(ns, 'baz')
    assert getattr(ns, 'baz') == 3.14

def test_ensure_value_with_none_value():
    class Namespace:
        pass
    
    ns = Namespace()
    assert ensure_value(ns, 'foo', None) is None
    # Ensure the attribute has been added with a None value
    assert hasattr(ns, 'foo')
    assert getattr(ns, 'foo') is None
