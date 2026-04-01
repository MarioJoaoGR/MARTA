
import re
import pytest
from string_utils.validation import is_number, InvalidInputError

def test_invalid_inputs():
    # Test cases with non-numeric strings
    assert not is_number('abc')
    assert not is_number('123abc')
    assert not is_number('12.34.56')
    
    # Test cases with None values
    with pytest.raises(InvalidInputError):
        is_number(None)
    
    # Test cases with empty strings
    assert not is_number('')
