
import pytest
from httpie.cli.requestitems import KeyValueArg

def process_query_param_arg(arg: KeyValueArg) -> str:
    return arg.value

# Test case for valid input
def test_valid_input():
    query_param = KeyValueArg()
    query_param.key = 'name'
    query_param.value = 'John Doe'
    
    result = process_query_param_arg(query_param)
    assert result == 'John Doe'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_requestitems_process_query_param_arg_1_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_process_query_param_arg_1_test_valid_input.py:10:18: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_process_query_param_arg_1_test_valid_input.py:10:18: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_process_query_param_arg_1_test_valid_input.py:10:18: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_process_query_param_arg_1_test_valid_input.py:10:18: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""