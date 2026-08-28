# Module: apimd.parser
# Import the function from its module
from apimd.parser import _table_cell

import pytest
from typing import Iterable

# Test cases for _table_cell function
def test_table_cell_with_items():
    assert _table_cell(['Item1', 'Item2']) == '| Item1 | Item2 |'
    # Additional test to ensure the order of items is preserved
    assert _table_cell(['First', 'Second']) == '| First | Second |'

def test_table_cell_with_empty_list():
    assert _table_cell([]) == '||'

def test_table_cell_with_single_item():
    assert _table_cell(['SingleItem']) == '| SingleItem |'

# Edge case: Test with a very long string to ensure it handles large inputs well
def test_table_cell_large_input():
    items = ['a'] * 100  # Create a list of 100 identical strings
    expected_output = '|' + '|'.join(f" {t} " for t in items) + '|'
    assert _table_cell(items) == expected_output

# Edge case: Test with special characters to ensure they are handled correctly
def test_table_cell_special_characters():
    assert _table_cell(['Item!', 'Item@']) == '| Item! | Item@ |'

# Negative test: Ensure it raises an error if the input is not iterable
def test_table_cell_non_iterable():
    with pytest.raises(TypeError):
        _table_cell(123)  # Passing a non-iterable integer to trigger TypeError
