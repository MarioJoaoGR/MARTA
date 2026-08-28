
import pytest
from apimd.parser import _table_split



def test_empty_input():
    args = []
    expected = '||'
    assert _table_split(args) == expected