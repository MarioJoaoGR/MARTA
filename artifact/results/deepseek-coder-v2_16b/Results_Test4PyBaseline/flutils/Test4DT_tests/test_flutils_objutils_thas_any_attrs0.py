
import pytest
from flutils.objutils import has_any_attrs

# Test cases for has_any_attrs function

def test_has_any_attrs_with_callable():
    class ExampleClass:
        def get(self):
            return "Hello"
        def keys(self):
            return ["key1", "key2"]
    
    example = ExampleClass()
    assert has_any_attrs(example, 'get', 'keys') == True

def test_has_any_attrs_with_callable_and_non_callable():
    class NonCallableExample:
        def get(self):
            return "Hello"
        def keys(self):
            return ["key1", "key2"]
    
    example = NonCallableExample()
    assert has_any_attrs(example, 'get', 'keys', 'foo') == True

def test_has_any_attrs_without_callable():
    class NoCallables:
        pass
    
    no_callables = NoCallables()