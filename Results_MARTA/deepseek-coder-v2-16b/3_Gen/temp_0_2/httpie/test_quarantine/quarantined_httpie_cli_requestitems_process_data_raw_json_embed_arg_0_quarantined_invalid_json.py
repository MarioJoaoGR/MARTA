
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import KeyValueArg, process_data_raw_json_embed_arg

def test_invalid_json():
    arg = KeyValueArg(value='{"name": "John", "age": 30, "city": "New York"}')
    
    with patch('httpie.cli.requestitems.load_json', side_effect=ValueError("Invalid JSON")):
        with pytest.raises(ValueError) as excinfo:
            process_data_raw_json_embed_arg(arg)
        
        assert str(excinfo.value) == "Invalid JSON"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_requestitems_process_data_raw_json_embed_arg_0_test_invalid_json
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_process_data_raw_json_embed_arg_0_test_invalid_json.py:7:10: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_process_data_raw_json_embed_arg_0_test_invalid_json.py:7:10: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_process_data_raw_json_embed_arg_0_test_invalid_json.py:7:10: E1120: No value for argument 'orig' in constructor call (no-value-for-parameter)


"""