# Module: pymonet.monad_try
# test_monad_try.py
from pymonet.monad_try import Try
import pytest

# Define a simple function to be encapsulated in Try
def divide(a, b):
    return a / b

# Define a function that raises a ZeroDivisionError
def divide_by_zero(a, b):
    return a / b

# Test cases for the of method with a successful function call
def test_of_successful():
    try_instance = Try.of(divide, 10, 2)
    assert try_instance.value == 5.0
    assert try_instance.is_success is True

# Test cases for the of method with a function call that raises an exception
def test_of_failure():
    try_failure = Try.of(divide_by_zero, 10, 0)
    assert str(try_failure.value) == "division by zero"
    assert try_failure.is_success is False

# Test cases for the of method with a lambda function that results in success
def test_of_lambda_successful():
    try_lambda = Try.of(lambda x, y: x + y, 5, 3)
    assert try_lambda.value == 8
    assert try_lambda.is_success is True

# Test cases for the of method with a lambda function that raises an exception
def test_of_lambda_failure():
    try_lambda_failure = Try.of(lambda x, y: x / y, 10, 0)
    assert str(try_lambda_failure.value) == "division by zero"
    assert try_lambda_failure.is_success is False

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
