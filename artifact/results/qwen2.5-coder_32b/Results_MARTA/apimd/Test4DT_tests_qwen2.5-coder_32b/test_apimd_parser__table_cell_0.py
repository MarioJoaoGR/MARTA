
import pytest
from apimd.parser import _table_cell

def test_valid_inputs_list():
    """Test valid inputs with a list of strings."""
    result = _table_cell(['Alice', '30', 'New York'])
    assert result == '| Alice | 30 | New York |'

def test_valid_inputs_tuple():
    """Test valid inputs with a tuple of strings."""
    result = _table_cell(('Bob', '25', 'Los Angeles'))
    assert result == '| Bob | 25 | Los Angeles |'

def test_empty_input():
    """Test empty input list."""
    result = _table_cell([])
    assert result == '||'


