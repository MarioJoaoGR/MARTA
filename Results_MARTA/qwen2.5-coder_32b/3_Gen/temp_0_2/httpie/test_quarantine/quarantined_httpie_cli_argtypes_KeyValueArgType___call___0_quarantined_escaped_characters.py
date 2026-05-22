
import argparse
from unittest.mock import patch
from httpie.cli.argtypes import KeyValueArgType, ArgumentTypeError

def test_escaped_characters():
    key_value_parser = KeyValueArgType('\\=')
    
    with patch('httpie.cli.argtypes.KeyValueArg', autospec=True) as mock_KeyValueArg:
        # Test case for escaped characters
        kv_pair = key_value_parser(r'foo\=bar')
        
        assert isinstance(kv_pair, mock_KeyValueArg)
        assert kv_pair.key == "foo"
        assert kv_pair.value == "bar"
        assert kv_pair.sep == '='
        assert kv_pair.orig == r'foo\=bar'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_argtypes_KeyValueArgType___call___0_test_escaped_characters
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType___call___0_test_escaped_characters.py:4:0: E0611: No name 'ArgumentTypeError' in module 'httpie.cli.argtypes' (no-name-in-module)


"""