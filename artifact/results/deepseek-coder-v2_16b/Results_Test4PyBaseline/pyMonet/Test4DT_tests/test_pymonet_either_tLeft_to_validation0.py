
# Module: pymonet.either
# test_left.py
from pymonet.either import Left
import pytest

@pytest.fixture
def left_instance():
    instance = Left("Some error message")  # Corrected constructor call with value argument
    return instance

def test_to_validation(left_instance):
    validation_result = left_instance.to_validation()
    assert validation_result.errors == ['Some error message']
