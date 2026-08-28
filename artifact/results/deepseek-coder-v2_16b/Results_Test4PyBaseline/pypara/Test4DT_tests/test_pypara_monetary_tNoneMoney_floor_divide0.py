# Module: pypara.monetary
# Import the function from the module
from pypara.monetary import NoneMoney as Money

import pytest

# Create an instance of NoneMoney
@pytest.fixture
def none_money():
    return Money()

# Test cases for floor_divide method
def test_floor_divide_with_integer(none_money):
    # Arrange
    other = 3
    
    # Act
    result = none_money.floor_divide(other)
    
    # Assert
    assert isinstance(result, Money), "Expected the result to be an instance of Money"
    assert result == none_money, "Expected the result to be equal to the original NoneMoney object"

def test_floor_divide_with_float(none_money):
    # Arrange
    other = 3.0
    
    # Act
    result = none_money.floor_divide(other)
    
    # Assert
    assert isinstance(result, Money), "Expected the result to be an instance of Money"
    assert result == none_money, "Expected the result to be equal to the original NoneMoney object"

def test_floor_divide_with_negative_integer(none_money):
    # Arrange
    other = -3
    
    # Act
    result = none_money.floor_divide(other)
    
    # Assert
    assert isinstance(result, Money), "Expected the result to be an instance of Money"
    assert result == none_money, "Expected the result to be equal to the original NoneMoney object"

def test_floor_divide_with_negative_float(none_money):
    # Arrange
    other = -3.0
    
    # Act
    result = none_money.floor_divide(other)
    
    # Assert
    assert isinstance(result, Money), "Expected the result to be an instance of Money"
    assert result == none_money, "Expected the result to be equal to the original NoneMoney object"
