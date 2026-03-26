
from unittest.mock import patch, sentinel
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing

def get_only(cls):
    return sentinel.get_only

@pytest.mark.parametrize("expected", [sentinel.get_only])
def test_edge_case(expected):
    with patch('pytutils.ext.rwclassproperty.sentinel', sentinel):
        z = Z()
        assert get_only(Z) == expected
