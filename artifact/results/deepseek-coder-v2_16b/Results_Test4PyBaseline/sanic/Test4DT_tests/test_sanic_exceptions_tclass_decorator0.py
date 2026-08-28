# Module: sanic.exceptions
import pytest
from sanic.exceptions import class_decorator

# Define a class to be decorated
class MyExceptionClass:
    pass

@pytest.fixture(autouse=True)
def reset_sanic_exceptions():
    # Reset the _sanic_exceptions dictionary before each test
    class_decorator._sanic_exceptions = {}

# Test case 1: Basic usage with status code 404 and quiet set to True by default if not provided
@class_decorator(MyExceptionClass, code=404)
class MyExceptionClass:
    pass

def test_class_decorator_basic():
    assert hasattr(MyExceptionClass, 'status_code')
    assert MyExceptionClass.status_code == 404
    assert getattr(MyExceptionClass, 'quiet', False) is True
    assert class_decorator._sanic_exceptions[404] is MyExceptionClass

# Test case 2: Usage with status code 500 and quiet set to False explicitly
@class_decorator(MyExceptionClass, code=500)
class MyExceptionClass:
    pass

def test_class_decorator_with_status_code_500():
    assert hasattr(MyExceptionClass, 'status_code')
    assert MyExceptionClass.status_code == 500
    assert getattr(MyExceptionClass, 'quiet', False) is False
    assert class_decorator._sanic_exceptions[500] is MyExceptionClass

# Test case 3: Usage with status code 404 and quiet set to False explicitly
@class_decorator(MyExceptionClass, code=404)
class MyExceptionClass:
    pass

def test_class_decorator_with_status_code_404():
    assert hasattr(MyExceptionClass, 'status_code')
    assert MyExceptionClass.status_code == 404
    assert getattr(MyExceptionClass, 'quiet', False) is True
    assert class_decorator._sanic_exceptions[404] is MyExceptionClass

# Test case 4: Usage with status code 404 and quiet set to None (should default to True if not provided)
@class_decorator(MyExceptionClass, code=404)
class MyExceptionClass:
    pass

def test_class_decorator_with_status_code_404_quiet_none():
    assert hasattr(MyExceptionClass, 'status_code')
    assert MyExceptionClass.status_code == 404
    assert getattr(MyExceptionClass, 'quiet', False) is True
    assert class_decorator._sanic_exceptions[404] is MyExceptionClass
