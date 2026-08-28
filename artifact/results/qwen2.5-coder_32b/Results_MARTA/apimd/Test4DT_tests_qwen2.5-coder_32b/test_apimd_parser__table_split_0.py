
import pytest
from apimd.parser import _table_split

def test__table_split_basic():
    headers = ["Name", "Age", "City"]
    expected_output = '|:----:|:---:|:----:|'
    assert _table_split(headers) == expected_output
