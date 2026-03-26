
import pytest
from pymonet.semigroups import All

def test_invalid_case_none():
    operand1 = All(None)  # Create an instance with value None
    operand2 = All(True)   # Create an instance with value True
    
    # Perform the concatenation
    result = operand1.concat(operand2)
    
    # Assert that the result is a new instance of All with value False
    assert isinstance(result, All)
    assert not result.value
