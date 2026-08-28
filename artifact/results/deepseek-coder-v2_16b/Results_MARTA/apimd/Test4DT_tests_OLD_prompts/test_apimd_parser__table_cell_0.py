
import pytest
from apimd.parser import _table_cell

def test_valid_input():
    assert _table_cell(['col1', 'col2']) == '| col1 | col2 |'

def test_invalid_input():
    with pytest.raises(TypeError):
        _table_cell()
