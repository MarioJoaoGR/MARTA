
import pytest
from unittest.mock import patch
from flutils.objutils import has_callables, has_attrs

# Scenario 1: Object with callable attributes
class TestClass:
    def method(self):
        pass

    @staticmethod
    def static_method():
        pass

def test_has_callables_with_callable_attributes():
    obj = TestClass()
    assert has_callables(obj, 'method', 'static_method') is True

# Scenario 2: Object with no callable attributes
class NoCallable:
    def __init__(self):
        self.attr1 = "value"
        self.attr2 = 42

def test_has_callables_with_no_callable_attributes():
    obj = NoCallable()
    assert has_callables(obj, 'attr1', 'attr2') is False

# Scenario 3: Object with one non-callable attribute
class MixedAttributes:
    def method(self):
        pass

def test_has_callables_with_one_non_callable_attribute():
    obj = MixedAttributes()
    assert has_callables(obj, 'method', 'non_existent_attr') is False

# Scenario 4: Using with built-in types
def test_has_callables_with_builtin_types():
    with patch('flutils.objutils.has_attrs', return_value=True):
        assert has_callables(dict(), 'get', 'keys') is True

# Scenario 5: Edge case: empty object and attributes
class EmptyClass:
    pass

def test_has_callables_with_empty_object():
    obj = EmptyClass()
    assert has_callables(obj, 'non_existent_attr') is False
