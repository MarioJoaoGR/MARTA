
import pytest
from apimd.parser import Parser

def test_valid_case():
    p = Parser()
    p.level['ExampleName'] = 2
    result = p._Parser__names_cmp('ExampleName')
    assert result == (2, 'examplename', True)

def test_edge_case_empty_string():
    p = Parser()
    with pytest.raises(KeyError):
        p._Parser__names_cmp('')

def test_invalid_case_missing_name():
    p = Parser()
    with pytest.raises(KeyError):
        p._Parser__names_cmp('MissingName')
