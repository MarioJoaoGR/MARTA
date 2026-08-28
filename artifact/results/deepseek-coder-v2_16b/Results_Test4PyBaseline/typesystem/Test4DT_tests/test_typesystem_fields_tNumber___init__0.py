
import pytest
from typesystem.fields import Number
from decimal import Decimal

# Test initialization with valid constraints
def test_number_initialization_valid():
    number = Number(minimum=0, maximum=10, exclusive_minimum=5, exclusive_maximum=9, precision="2", multiple_of=3)
    assert number.minimum == 0
    assert number.exclusive_minimum == 5
    assert number.maximum == 10
    assert number.exclusive_maximum == 9
    assert number.precision == "2"