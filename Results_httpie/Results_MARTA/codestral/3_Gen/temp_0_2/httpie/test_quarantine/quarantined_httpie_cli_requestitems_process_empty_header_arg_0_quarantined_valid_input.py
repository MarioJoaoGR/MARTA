
import pytest
from httpie.cli.requestitems import KeyValueArg, ParseError

def process_empty_header_arg(arg: KeyValueArg) -> str:
    if not arg.value:
        return arg.value
    raise ParseError(
        f'Invalid item {arg.orig!r} (to specify an empty header use `Header;`)'
    )

def test_valid_input():
    # Test case for valid input where the argument is an empty header
    with pytest.raises(ParseError) as exc_info:
        process_empty_header_arg(KeyValueArg(orig='Header;', value=''))
    assert str(exc_info.value) == ''

    # Additional test case to ensure it raises a ParseError for non-empty headers
    with pytest.raises(ParseError) as exc_info:
        process_empty_header_arg(KeyValueArg(orig='SomeOtherKey', value='value'))
    assert str(exc_info.value) == "Invalid item 'SomeOtherKey' (to specify an empty header use `Header;`)"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_requestitems_process_empty_header_arg_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_empty_header_arg_0_test_valid_input.py:15:33: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_empty_header_arg_0_test_valid_input.py:15:33: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_empty_header_arg_0_test_valid_input.py:20:33: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_empty_header_arg_0_test_valid_input.py:20:33: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)


"""