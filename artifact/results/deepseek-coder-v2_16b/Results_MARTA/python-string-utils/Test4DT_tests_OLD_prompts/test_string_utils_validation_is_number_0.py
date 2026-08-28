
import pytest
from string_utils.validation import is_number, InvalidInputError
import re
from unittest.mock import patch

# Define the regex pattern for a valid number
NUMBER_RE = re.compile(r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$")

def test_valid_numbers():
    assert is_number('42') == True
    assert is_number('-9.12') == True
    assert is_number('1e3') == True

@pytest.mark.xfail(raises=InvalidInputError)
def test_invalid_inputs():
    with pytest.raises(InvalidInputError):
        is_number(None)

@pytest.mark.xfail(raises=InvalidInputError)
def test_edge_cases():
    assert is_number(str(2**63 - 1)) == True
    assert is_number(str(-2**63)) == True
