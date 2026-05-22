
import pytest
from httpie.cli.requestitems import KeyValueArg, ParseError

def process_empty_header_arg(arg: KeyValueArg) -> str:
    if not arg.value:
        return arg.value
    raise ParseError(
        f'Invalid item {arg.orig!r} (to specify an empty header use `Header;`)'
    )

def test_none_input():
    with pytest.raises(ParseError) as excinfo:
        process_empty_header_arg(KeyValueArg(orig='SomeOtherKey', value=None))
    assert str(excinfo.value) == 'Invalid item SomeOtherKey (to specify an empty header use `Header;`)'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_requestitems_process_empty_header_arg_0_test_none_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_process_empty_header_arg_0_test_none_input.py:14:33: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_process_empty_header_arg_0_test_none_input.py:14:33: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)


"""