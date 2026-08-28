
import pytest
from flutils.namedtupleutils import _to_namedtuple

# Test cases for _to_namedtuple function

def test_conversion_with_valid_dict():
    # Arrange
    input_obj = {'name': 'John', 'age': 30}
    
    # Act
    result = _to_namedtuple(input_obj, True)
    
    # Assert
    assert isinstance(result, tuple), "Expected a named tuple"
    assert len(result) == 2, "Expected the named tuple to have two elements"