
import pytest
from httpie.cli.argtypes import KeyValueArgType

@pytest.fixture
def key_value_parser():
    return KeyValueArgType()

def test_valid_input(key_value_parser):
    # Test with a valid input string
    result = key_value_parser('foo=bar')
    assert result.key == 'foo'
    assert result.value == 'bar'
    assert result.sep == '='
    assert result.orig == 'foo=bar'

    # Test with a valid input string using a different separator
    result = key_value_parser('foo:bar', separators=[':', ','])
    assert result.key == 'foo'
    assert result.value == 'bar'
    assert result.sep == ':'
    assert result.orig == 'foo:bar'

    # Test with an invalid input string
    with pytest.raises(argparse.ArgumentTypeError):
        key_value_parser('foobar')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_argtypes_KeyValueArgType___call___0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType___call___0_test_valid_input.py:25:23: E0602: Undefined variable 'argparse' (undefined-variable)


"""