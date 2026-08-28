
import pytest
from pymonet.either import Left

# Test valid input scenario
def test_valid_input():
    left_instance = Left('error message')
    result = left_instance.bind(lambda x: x + 1)
    assert isinstance(result, Left)
    assert result.value == 'error message'

# Test None input scenario
def test_none_input():
    left_instance = Left(None)
    result = left_instance.bind(lambda x: x + 1)
    assert isinstance(result, Left)
    assert result.value is None

# Test invalid input scenario
def test_invalid_input():
    left_instance = Left('error message')
    with pytest.raises(TypeError):
        left_instance.bind()
