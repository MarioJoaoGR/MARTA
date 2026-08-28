
# Module: pytutils.props
# Import the function correctly using its module name.
from pytutils.props import lazyclassproperty

import pytest

# Define a class with a lazy/cached class property for testing
class TestClass:
    @lazyclassproperty
    def expensive_calculation(self):  # Added 'self' as the first argument
        print("Calculating...")
        return sum(range(1000))

# Test cases for the lazyclassproperty decorator
def test_first_call():
    # First call should calculate and cache the result
    assert TestClass().expensive_calculation == 499500, "First call to expensive_calculation did not calculate correctly."

def test_subsequent_calls():
    # Subsequent calls should return the cached result
    instance = TestClass()
    assert instance.expensive_calculation == 499500, "Subsequent calls to expensive_calculation did not retrieve the cached result."

# Additional tests for different calculations
class AnotherTestClass:
    @lazyclassproperty
    def complex_computation(self):  # Added 'self' as the first argument
        print("Computing...")
        return max([i**2 for i in range(100)])

def test_another_first_call():
    # First call should compute and cache the result
    assert AnotherTestClass().complex_computation == 9801, "First call to complex_computation did not compute correctly."

def test_another_subsequent_calls():
    # Subsequent calls should return the cached result
    instance = AnotherTestClass()
    assert instance.complex_computation == 9801, "Subsequent calls to complex_computation did not retrieve the cached result."

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
