
import argparse
from httpie.cli.argtypes import parse_format_options
from unittest.mock import patch

def test_invalid_input():
    with patch('httpie.cli.argtypes.argparse') as mock_argparse:
        # Test case for invalid input
        s = 'json.indent:2,json.sort_keys:false'  # Invalid boolean value
        defaults = {'json': {'indent': 4, 'sort_keys': True}}
        
        try:
            parse_format_options(s, defaults)
        except argparse.ArgumentTypeError as e:
            assert str(e) == "invalid value 'false' in 'json.sort_keys:false' (expected <class 'bool'> got <class 'str'>)"
