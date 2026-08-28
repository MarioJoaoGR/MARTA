# Module: sanic.mixins.exceptions
import pytest
from sanic.mixins.exceptions import decorator

# Example Call 1: Basic Usage
def test_basic_usage():
    def my_handler(data):
        if some_condition:
            raise ValueError("Invalid data")
        return processed_data

    handler = decorator(my_handler, exceptions=(ValueError,))

    with pytest.raises(ValueError) as exc_info:
        result = handler({"some": "input"})
    assert str(exc_info.value) == "Invalid data"

# Example Call 2: Custom Exception Handling
def test_custom_exception_handling():
    class MyCustomException(Exception):
        pass

    def my_custom_handler(data):
        if another_condition:
            raise MyCustomException("Something went wrong")
        return processed_data

    handler = decorator(my_custom_handler, exceptions=(MyCustomException,))

    with pytest.raises(MyCustomException) as exc_info:
        result = handler({"some": "input"})
    assert str(exc_info.value) == "Something went wrong"

# Example Call 3: Applying Decorator Immediately
class ImmediateException(Exception):
    pass

def test_apply_decorator_immediately():
    def immediate_handler(data):
        if yet_another_condition:
            raise ImmediateException("An immediate issue occurred")
        return processed_data

    decorated_handler = decorator(immediate_handler, exceptions=(ImmediateException,), apply=True)

    with pytest.raises(ImmediateException) as exc_info:
        result = decorated_handler({"some": "input"})
    assert str(exc_info.value) == "An immediate issue occurred"

# Example Call 4: Handling Multiple Exceptions
def test_handling_multiple_exceptions():
    def multi_exception_handler(data):
        if yet_another_condition:
            raise ValueError("Value error")
        elif another_condition:
            raise TypeError("Type error")
        return processed_data

    handler = decorator(multi_exception_handler, exceptions=(ValueError, TypeError))

    with pytest.raises(ValueError) as exc_info:
        result = handler({"some": "input"})
    assert str(exc_info.value) == "Value error"
