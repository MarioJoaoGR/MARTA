
import pytest
from pysnooper.tracer import Tracer

# Test case for invalid input to _wrap_class method
def test_wrap_class_invalid_inputs():
    tracer = Tracer()
    with pytest.raises(AttributeError):
        tracer._wrap_class(42)

# Test case for valid class input to _wrap_class method
def test_wrap_class_valid_class():
    tracer = Tracer()

    class SampleClass:
        def sample_method(self, x):
            return x * 2

    wrapped_class = tracer._wrap_class(SampleClass)
    instance = wrapped_class()
    result = instance.sample_method(5)
    assert result == 10

# Test case for class with coroutine method
def test_wrap_class_with_coroutine():
    import asyncio

    tracer = Tracer()

    class SampleClass:
        async def sample_coroutine(self, x):
            return x * 2

    wrapped_class = tracer._wrap_class(SampleClass)
    instance = wrapped_class()
    result = asyncio.run(instance.sample_coroutine(5))
    assert result == 10

# Test case for class with multiple methods
def test_wrap_class_with_multiple_methods():
    tracer = Tracer()

    class SampleClass:
        def method_one(self, x):
            return x + 10

        def method_two(self, a, b):
            return a * b

    wrapped_class = tracer._wrap_class(SampleClass)
    instance = wrapped_class()
    result_one = instance.method_one(5)
    result_two = instance.method_two(3, 4)
    assert result_one == 15
    assert result_two == 12
