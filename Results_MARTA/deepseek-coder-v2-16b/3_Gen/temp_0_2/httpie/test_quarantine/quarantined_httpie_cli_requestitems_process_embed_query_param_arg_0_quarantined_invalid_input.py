
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import process_embed_query_param_arg, KeyValueArg

@pytest.mark.parametrize("invalid_input", [None, 123, {}])
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        arg = KeyValueArg(orig="test", value=invalid_input)
        process_embed_query_param_arg(arg)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_requestitems_process_embed_query_param_arg_0_test_invalid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_process_embed_query_param_arg_0_test_invalid_input.py:9:14: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_process_embed_query_param_arg_0_test_invalid_input.py:9:14: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)


"""