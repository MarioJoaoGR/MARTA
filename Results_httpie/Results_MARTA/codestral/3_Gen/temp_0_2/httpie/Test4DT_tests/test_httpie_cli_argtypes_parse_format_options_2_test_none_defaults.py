
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import parse_format_options

def test_none_defaults():
    with patch('httpie.cli.argtypes.deepcopy', return_value={'json': {'indent': 2, 'sort_keys': False}}):
        result = parse_format_options(s='json.indent:2,json.sort_keys:False', defaults=None)
        assert result == {'json': {'indent': 2, 'sort_keys': False}}
