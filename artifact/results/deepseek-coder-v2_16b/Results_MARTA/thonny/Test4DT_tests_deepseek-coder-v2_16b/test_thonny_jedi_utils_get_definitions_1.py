
import pytest
from thonny.jedi_utils import get_definitions


def test_invalid_input():
    source = "def hello() pass"
    filename = "example.py"
    row, column = 0, 4
    with pytest.raises(Exception):
        get_definitions(source, filename, row, column)