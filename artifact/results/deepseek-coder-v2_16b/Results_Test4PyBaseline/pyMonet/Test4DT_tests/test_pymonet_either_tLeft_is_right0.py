
# Module: pymonet.either
import pytest
from pymonet.either import Left, Right

# Test cases for the `is_right` method of the `Left` class
def test_left_instance():
    left_instance = Left(value=None)  # Corrected the constructor call to include a value parameter
    assert not left_instance.is_right(), "Expected is_right to return False for a Left instance"

# Test cases for the `is_left` method of the `Left` class
def test_left_instance_is_left():
    left_instance = Left(value=None)  # Corrected the constructor call to include a value parameter
    assert left_instance.is_left(), "Expected is_left to return True for a Left instance"

# Test cases for the `is_right` method of the `Right` class
def test_right_instance():
    right_instance = Right(value="success")  # Corrected the constructor call to include a value parameter
    assert right_instance.is_right(), "Expected is_right to return True for a Right instance"

# Test cases for the `map` method of the `Either` class (applicable to Right)
def test_right_instance_map():
    right_instance = Right(value=10)  # Corrected the constructor call to include a value parameter
    def add_one(x):
        return x + 1
    mapped_right = right_instance.map(add_one)
    assert mapped_right.value == 11, "Expected the map function to be applied to the value"

# Test cases for the `bind` method of the `Either` class (applicable to Right)
def test_right_instance_bind():
    right_instance = Right(value=10)  # Corrected the constructor call to include a value parameter
    def add_if_even(x):
        return x + 1 if isinstance(x, int) and x % 2 == 0 else None
    result = right_instance.bind(add_if_even)
    assert result == 11, "Expected the bind function to be applied to the value"

# Test cases for the `is_left` method of the `Right` class
def test_right_instance_is_left():
    right_instance = Right(value="success")  # Corrected the constructor call to include a value parameter
    assert not right_instance.is_left(), "Expected is_left to return False for a Right instance"

# Test cases for the `is_right` method of the `Right` class
def test_right_instance_is_right():
    right_instance = Right(value="success")  # Corrected the constructor call to include a value parameter
    assert right_instance.is_right(), "Expected is_right to return True for a Right instance"
