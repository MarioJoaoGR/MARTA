
import pytest
from pysnooper.tracer import Tracer
import pysnooper  # Importing pysnooper at the module level to avoid undefined variable issues

# Test cases for the Tracer class
def test_wrap_class_basic():
    tracer = Tracer()
    
    class MyClass:
        def my_method(self):
            return "hello"
    
    wrapped_cls = tracer._wrap_class(MyClass)
    assert hasattr(wrapped_cls, 'my_method')
    assert callable(getattr(wrapped_cls, 'my_method'))

def test_wrap_class_skip_coroutine():
    tracer = Tracer()
    
    class MyCoroutine:
        async def my_coro(self):
            return "hello"
    
    wrapped_cls = tracer._wrap_class(MyCoroutine)