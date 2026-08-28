
import pytest
from unittest.mock import patch
from blib2to3.pgen2.tokenize import group

def maybe(*choices):
    return group(*choices) + "?"

@pytest.mark.parametrize("choices_param, expected", [
    (('apple', 'banana', 'cherry'), '(apple|banana|cherry)?'),
    (('a', 'b', 'c', 'd'), '(a|b|c|d)?'),
    ([], '()?')
])
def test_valid_input(choices_param, expected):
    with patch('blib2to3.pgen2.tokenize.group', return_value=''):
        result = maybe(*choices_param)
        assert result == expected

def test_edge_case():
    with patch('blib2to3.pgen2.tokenize.group', return_value=''):
        result = maybe()
        assert result == '()?'
