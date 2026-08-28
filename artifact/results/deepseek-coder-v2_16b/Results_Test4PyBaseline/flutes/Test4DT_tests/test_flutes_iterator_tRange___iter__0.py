
import pytest
from flutes.iterator import Range

@pytest.fixture
def range_instance():
    return Range(10)

@pytest.fixture
def range_instance_with_start_end():
    return Range(1, 10 + 1)

@pytest.fixture
def range_instance_with_start_end_step():
    return Range(1, 11, 2)

def test_range_default_creation(range_instance):
    assert list(range_instance) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_range_with_start_end():
    r = Range(1, 10 + 1)
    assert list(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_range_with_start_end_step():
    r = Range(1, 11, 2)