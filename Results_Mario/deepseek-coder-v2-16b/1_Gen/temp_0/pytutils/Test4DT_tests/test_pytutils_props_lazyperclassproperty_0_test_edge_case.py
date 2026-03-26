
import pytest
from pytutils.props import lazyperclassproperty

# Mocking a class for testing purposes
class MockClass:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Test function to check the lazyperclassproperty decorator
def test_lazyperclassproperty():
    # Define a mock expensive calculation function
    def expensive_calculation(cls):
        return cls.__name__ + '_result'

    # Apply the lazyperclassproperty decorator to the expensive calculation function
    MockClass.cached_result = lazyperclassproperty(expensive_calculation)

    # Create an instance of MockClass
    mock_instance = MockClass()

    # Set the name attribute for the mock instance
    mock_instance.name = 'TestName'

    # Check if the cached result is correctly calculated and stored
    assert MockClass.cached_result == 'MockClass_result'
    assert mock_instance.cached_result == 'MockClass_result'
