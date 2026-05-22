
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import parse_format_options

def test_valid_input():
    with patch('httpie.cli.argtypes.deepcopy', return_value={'json': {'indent': 2, 'sort_keys': False}}):
        result = parse_format_options(
            defaults={'json': {'indent': 4, 'sort_keys': True}},
            s='json.indent:2,json.sort_keys:False'
        )
        assert result == {'json': {'indent': 2, 'sort_keys': False}}
