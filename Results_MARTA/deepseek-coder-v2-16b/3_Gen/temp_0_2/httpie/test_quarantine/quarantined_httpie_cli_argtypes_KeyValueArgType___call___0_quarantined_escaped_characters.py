
import pytest
from httpie.cli.argtypes import KeyValueArgType, ArgumentTypeError

def test_escaped_characters(key_value_parser):
    with pytest.raises(ArgumentTypeError) as excinfo:
        result = key_value_parser.parse("foo\\=bar")
    assert str(excinfo.value) == "Expected '=' separator"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_argtypes_KeyValueArgType___call___0_test_escaped_characters
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType___call___0_test_escaped_characters.py:3:0: E0611: No name 'ArgumentTypeError' in module 'httpie.cli.argtypes' (no-name-in-module)


"""