
import pytest
from pytutils.props import setterproperty

# Test fixture to create a mock setter property
@pytest.fixture
def create_mock_setterproperty():
    def _create_mock_setterproperty(func):
        return setterproperty(func)
    return _create_mock_setterproperty

# Test case for invalid input when setting the value
def test_invalid_input(create_mock_setterproperty):
    with pytest.raises(TypeError):
        class MyClass:
            def __init__(self, initial_value):
                self._value = initial_value
            
            @create_mock_setterproperty
            def value(self):
                return self._value
        
        obj = MyClass(10)
        obj.value = "invalid input"  # This should raise a TypeError
