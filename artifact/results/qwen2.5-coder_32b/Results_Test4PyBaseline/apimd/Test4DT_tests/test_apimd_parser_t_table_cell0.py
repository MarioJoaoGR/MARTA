
import pytest
from apimd.parser import _table_cell

def test_table_cell_with_multiple_items():
    assert _table_cell(["Alice", "30", "New York"]) == "| Alice | 30 | New York |"

def test_table_cell_with_two_items():
    assert _table_cell(["Bob", "25"]) == "| Bob | 25 |"

def test_table_cell_with_empty_strings():
    assert _table_cell(["", "", ""]) == "|  |  |  |"

def test_table_cell_with_single_character_strings():
    assert _table_cell(["A", "B", "C"]) == "| A | B | C |"

def test_table_cell_with_mixed_length_strings():
    assert _table_cell(["Short", "LongerString", "Medium"]) == "| Short | LongerString | Medium |"

def test_table_cell_with_single_item():
    assert _table_cell(["Single"]) == "| Single |"

def test_table_cell_with_no_items():
    assert _table_cell([]) == "||"
