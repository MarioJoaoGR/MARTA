
# Module: pymonet.either
# test_either.py
from pymonet.either import Right
import pytest

@pytest.fixture
def right_instance():
    return Right(42)

def test_bind_with_mapper(right_instance):
    """Test the bind method with a mapper function."""
    mapped_value = right_instance.bind(lambda x: x * 2)
    assert mapped_value == 84

def test_bind_with_invalid_mapper():
    """Test the bind method with an invalid mapper function."""
    right_instance = Right("valid")
    mapped_value = right_instance.bind(lambda x: x * 2)