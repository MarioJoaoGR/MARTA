
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import parse_format_options

@pytest.fixture(autouse=True)
def setup():
    s = 'json.indent:2,json.sort_keys:False'
    defaults = {'json': {'indent': 4, 'sort_keys': True}}
    return s, defaults

def test_none_defaults(setup):
    s, defaults = setup
    with patch('httpie.cli.argtypes.deepcopy', lambda x: x):
        result = parse_format_options(s, None)
        assert result == {'json': {'indent': 2, 'sort_keys': False}}
