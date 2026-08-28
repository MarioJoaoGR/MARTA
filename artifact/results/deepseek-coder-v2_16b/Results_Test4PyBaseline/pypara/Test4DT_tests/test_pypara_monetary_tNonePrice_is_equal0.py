
import pytest
from pypara.monetary import NonePrice

# Test initialization of NonePrice instance
def test_noneprice_initialization():
    np = NonePrice()
    assert isinstance(np, NonePrice), "Expected an instance of NonePrice"

# Test equality comparison with another NonePrice instance
def test_equality_comparison():
    np1 = NonePrice()
    np2 = NonePrice()
    assert np1 == np2, "Expected two instances of NonePrice to be equal"

# Test inequality comparison with a different type
def test_inequality_comparison():
    np = NonePrice()
    assert np != 10, "Expected an instance of NonePrice to be not equal to an integer"

# Test arithmetic operations with numeric types (treated as zero)
@pytest.mark.parametrize("operation", [lambda x: x + 10, lambda x: x - 5, lambda x: x * 2, lambda x: x / 2])
def test_arithmetic_operations(operation):
    np = NonePrice()
    result = operation(np)