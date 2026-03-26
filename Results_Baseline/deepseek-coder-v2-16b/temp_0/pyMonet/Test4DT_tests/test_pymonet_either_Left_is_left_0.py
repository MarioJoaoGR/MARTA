
# Module: pymonet.either
# Importing the Left class if not already imported
from pymonet.either import Left, Right  # Assuming Right is defined in the same module or correctly imported
import pytest

@pytest.fixture
def left_instance():
    return Left("error message")

def test_is_left(left_instance):
    assert left_instance.is_left() == True

def test_map(left_instance):
    mapped_left = left_instance.map(lambda x: x + " mapped")
    assert mapped_left.value == "error message"  # Corrected assertion to match the expected behavior

def test_bind(left_instance):
    bound_left = left_instance.bind(lambda x: Right(x + " bound"))  # Assuming bind method exists and returns a Right instance