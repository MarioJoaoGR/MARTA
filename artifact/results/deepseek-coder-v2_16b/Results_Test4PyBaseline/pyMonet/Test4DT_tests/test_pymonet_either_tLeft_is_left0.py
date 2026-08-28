
# Module: pymonet.either
# test_pymonet_either.py
from pymonet.either import Left
import pytest

@pytest.fixture
def left_instance():
    return Left(None)  # Corrected to provide a default value for the 'value' parameter

def test_is_left(left_instance):
    assert left_instance.is_left() == True

def test_is_right(left_instance):
    assert left_instance.is_right() == False
