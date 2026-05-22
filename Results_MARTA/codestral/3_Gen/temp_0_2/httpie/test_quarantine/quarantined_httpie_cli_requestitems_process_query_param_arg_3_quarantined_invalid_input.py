
import pytest
from httpie.cli.requestitems import KeyValueArg

def process_query_param_arg(arg: KeyValueArg) -> str:
    return arg.value

def test_invalid_input():
    with pytest.raises(AttributeError):
        query_param = KeyValueArg(key=123, value='John Doe')
        process_query_param_arg(query_param)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_requestitems_process_query_param_arg_3_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_query_param_arg_3_test_invalid_input.py:10:22: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_process_query_param_arg_3_test_invalid_input.py:10:22: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""