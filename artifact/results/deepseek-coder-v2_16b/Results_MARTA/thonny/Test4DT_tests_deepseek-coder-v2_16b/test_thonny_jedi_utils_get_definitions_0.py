
import pytest
from thonny.jedi_utils import get_definitions



def test_invalid_input():
    source = "def invalid_code():"
    filename = "example.py"
    row, column = 0, 4
    with pytest.raises(ValueError):
        get_definitions(source, row, column, filename)