
import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    try1 = Try(42, True)
    assert try1.value == 42
    assert try1.is_success is True

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Try()  # This should raise a TypeError because the constructor requires two arguments: value and is_success

def test_map_method():
    def double(x):
        return x * 2

    try1 = Try(42, True)
    mapped_try = try1.map(double)
    assert mapped_try.value == 84
    assert mapped_try.is_success is True

def test_bind_method():
    def divide_by_two(x):
        if x % 2 == 0:
            return Try(x / 2, True)
        else:
            return Try(None, False)

    try1 = Try(42, True)
    bound_try = try1.bind(divide_by_two)
    assert bound_try.is_success is True
    assert bound_try.value == 21.0

def test_on_success():
    def log_success(value):
        print(f"Success! The value is {value}")

    try1 = Try(42, True)
    try1.on_success(log_success)

def test_on_fail():
    def log_failure(value):
        print(f"Failure! The error is {value}")

    try2 = Try("error", False)
    try2.on_fail(log_failure)
