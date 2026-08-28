
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    try1 = Try(42, True)
    assert isinstance(try1, Try)
    assert try1.value == 42
    assert try1.is_success is True

def test_invalid_input():
    with pytest.raises(TypeError):
        Try()

def test_eq_method():
    try1 = Try(42, True)
    try2 = Try(42, True)
    assert try1 == try2

    try3 = Try("error", False)
    try4 = Try("error", False)
    assert try3 == try4

def test_map_method():
    def double_value(x):
        return x * 2

    try1 = Try(42, True)
    mapped_try = try1.map(double_value)
    assert isinstance(mapped_try, Try)
    assert mapped_try.get() == 84

def test_bind_method():
    def divide_by_two(x):
        if x % 2 == 0:
            return Try(x // 2, True)
        else:
            return Try(None, False)

    try1 = Try(42, True)
    bound_try = try1.bind(divide_by_two)
    assert isinstance(bound_try, Try)
    assert bound_try.get() == 21

def test_on_success_method():
    def print_value(x):
        print("Success:", x)

    try1 = Try(42, True)
    try1.on_success(print_value)

def test_on_fail_method():
    def print_error(x):
        print("Error:", x)

    try2 = Try("error", False)
    try2.on_fail(print_error)
