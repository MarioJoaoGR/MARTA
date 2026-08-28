
import pytest
from apimd.parser import _table_split

def test_table_split_basic():
    assert _table_split(["Name", "Age", "City"]) == '|:----:|:---:|:----:|'

def test_table_split_long_headers():
    assert _table_split(["FirstName", "LastName", "Address"]) == '|:---------:|:--------:|:-------:|'

def test_table_split_mixed_length_headers():
    assert _table_split(["ID", "Description", "Qty"]) == '|:---:|:-----------:|:---:|'

def test_table_split_single_column():
    assert _table_split(["Header"]) == '|:------:|'

def test_table_split_empty_header():
    assert _table_split(["", "Header"]) == '|:---:|:------:|'

def test_table_split_minimum_width():
    assert _table_split(["A", "BB", "CCC"]) == '|:---:|:---:|:---:|'

def test_table_split_all_short_headers():
    assert _table_split(["X", "Y", "Z"]) == '|:---:|:---:|:---:|'
