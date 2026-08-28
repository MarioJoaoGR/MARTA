
import pytest
from apimd.parser import Parser

def test_valid_input():
    p = Parser()
    p.level = {'name1': 1, 'name2': 2}
    result = p._Parser__names_cmp('name1')
    assert result == (1, 'name1', False)

def test_invalid_input():
    p = Parser()
    with pytest.raises(KeyError):
        p._Parser__names_cmp('non_existent_name')
