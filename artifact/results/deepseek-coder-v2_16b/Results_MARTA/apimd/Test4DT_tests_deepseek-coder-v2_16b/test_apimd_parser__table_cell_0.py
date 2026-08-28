
import pytest
from apimd.parser import _table_cell


def test_empty_input():
    items = []
    expected_output = '||'
    assert _table_cell(items) == expected_output

def test_single_item_input():
    items = ['single item']
    expected_output = '| single item |'
    assert _table_cell(items) == expected_output