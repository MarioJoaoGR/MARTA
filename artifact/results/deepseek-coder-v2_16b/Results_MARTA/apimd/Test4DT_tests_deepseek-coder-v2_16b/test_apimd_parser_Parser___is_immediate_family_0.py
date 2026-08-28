
import pytest
from apimd.parser import Parser


def test_edge_case():
    p = Parser()
    p.root['empty'] = ''
    p.root['nonexistent'] = 'non'
    with pytest.raises(KeyError):
        assert p._Parser__is_immediate_family('example', 'other') == False