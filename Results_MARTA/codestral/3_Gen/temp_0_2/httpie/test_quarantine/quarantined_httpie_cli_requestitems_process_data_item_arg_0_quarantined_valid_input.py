
import pytest
from httpie.cli.requestitems import KeyValueArg

def process_data_item_arg(arg: KeyValueArg) -> str:
    return arg.value

@pytest.mark.parametrize("arg", [KeyValueArg(key='data', value='some data')])
def test_valid_input(arg):
    result = process_data_item_arg(arg)
    assert result == 'some data'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_requestitems_process_data_item_arg_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_data_item_arg_0_test_valid_input.py:8:33: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_data_item_arg_0_test_valid_input.py:8:33: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""