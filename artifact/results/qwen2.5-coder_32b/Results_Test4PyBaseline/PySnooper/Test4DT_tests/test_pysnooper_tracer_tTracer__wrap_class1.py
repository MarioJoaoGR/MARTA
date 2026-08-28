
import inspect
from unittest.mock import MagicMock, create_autospec
from pysnooper.tracer import Tracer

# Mocking pycompat since it cannot be imported
class MockPyCompat:
    iscoroutinefunction = MagicMock()

pycompat = MockPyCompat()

def test_wrap_class_no_attributes():
    """Test wrapping a class with no attributes."""
    tracer = Tracer()
    cls = type('TestClass', (object,), {})
    
    wrapped_cls = tracer._wrap_class(cls)
    assert wrapped_cls is cls  # No changes expected

def test_wrap_class_with_regular_function():
    """Test wrapping a class with a regular function attribute."""
    tracer = Tracer()
    def sample_function(x):
        return x * 2
    
    cls = type('TestClass', (object,), {'sample_function': sample_function})
    
    wrapped_cls = tracer._wrap_class(cls)
    assert callable(wrapped_cls.sample_function)  # Ensure it's still callable
    assert wrapped_cls.sample_function(5) == 10  # Ensure function behavior is preserved

def test_wrap_class_with_coroutine():
    """Test wrapping a class with a coroutine function attribute."""
    tracer = Tracer()
    
    async def sample_coroutine(x):
        return x * 2
    
    cls = type('TestClass', (object,), {'sample_coroutine': sample_coroutine})
    
    pycompat.iscoroutinefunction.return_value = True
    wrapped_cls = tracer._wrap_class(cls)
    assert wrapped_cls.sample_coroutine is sample_coroutine  # Ensure coroutine is not wrapped

def test_wrap_class_with_mixed_attributes():
    """Test wrapping a class with both regular and coroutine functions."""
    tracer = Tracer()
    
    def sample_function(x):
        return x * 2
    
    async def sample_coroutine(x):
        return x * 2
    
    cls = type('TestClass', (object,), {
        'sample_function': sample_function,
        'sample_coroutine': sample_coroutine
    })
    
    pycompat.iscoroutinefunction.side_effect = lambda attr: attr.__name__ == 'sample_coroutine'
    wrapped_cls = tracer._wrap_class(cls)
    
    assert callable(wrapped_cls.sample_function)  # Ensure regular function is wrapped
    assert wrapped_cls.sample_function(5) == 10  # Ensure function behavior is preserved
    
    assert wrapped_cls.sample_coroutine is sample_coroutine  # Ensure coroutine is not wrapped

def test_wrap_class_with_non_function_attributes():
    """Test wrapping a class with non-function attributes."""
    tracer = Tracer()
    
    cls = type('TestClass', (object,), {
        'sample_variable': 42,
        'sample_list': [1, 2, 3]
    })
    
    wrapped_cls = tracer._wrap_class(cls)
    assert wrapped_cls.sample_variable == 42
    assert wrapped_cls.sample_list == [1, 2, 3]

def test_wrap_class_with_wrapped_function_behavior():
    """Test that the wrapped function behaves as expected."""
    tracer = Tracer()
    
    def sample_function(x):
        return x * 2
    
    cls = type('TestClass', (object,), {'sample_function': sample_function})
    
    wrapped_cls = tracer._wrap_class(cls)
    assert callable(wrapped_cls.sample_function)  # Ensure it's still callable
    assert wrapped_cls.sample_function(5) == 10  # Ensure function behavior is preserved

# Mocking _wrap_function to ensure it wraps correctly
tracer_mock = create_autospec(Tracer)
tracer_mock._wrap_function.return_value = lambda x: x * 3

def test_wrap_class_with_wrapped_function():
    """Test that the wrapped function is replaced with a new function."""
    tracer = Tracer()
    
    def sample_function(x):
        return x * 2
    
    cls = type('TestClass', (object,), {'sample_function': sample_function})
    
    # Patch _wrap_function to return a different behavior
    original_wrap_function = tracer._wrap_function
    tracer._wrap_function = lambda func: lambda x: x * 3
    
    wrapped_cls = tracer._wrap_class(cls)
    assert callable(wrapped_cls.sample_function)  # Ensure it's still callable
    assert wrapped_cls.sample_function(5) == 15  # Ensure function behavior is changed as expected
    
    # Restore original _wrap_function
    tracer._wrap_function = original_wrap_function
