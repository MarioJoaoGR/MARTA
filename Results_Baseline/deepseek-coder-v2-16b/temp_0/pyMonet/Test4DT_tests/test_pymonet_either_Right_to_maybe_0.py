
# Module: pymonet.either
# test_right.py
from pymonet.either import Right
import pytest
from pymonet.maybe import Maybe

@pytest.fixture
def right_with_value():
    return Right(value=42)

@pytest.fixture
def error_right():
    return Right(None)  # Corrected the argument to match the constructor definition

def test_to_maybe_with_value(right_with_value):
    maybe = right_with_value.to_maybe()
    assert not maybe.is_nothing
    assert maybe.value == 42

def test_to_maybe_without_value(error_right):
    maybe = error_right.to_maybe()