
import json
from typing import Tuple
from unittest.mock import patch, MagicMock
from httpie.output.utils import load_prefixed_json, load_json_preserve_order_and_dupe_keys

def test_valid_input():
    with patch('httpie.output.utils.load_json_preserve_order_and_dupe_keys', autospec=True) as mock_load_json:
        data = '__XSSI_PREFIX__ {"name": "John", "age": 30, "city": "New York"}'
        expected_prefix = '__XSSI_PREFIX__'
        expected_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
        
        result = load_prefixed_json(data)
        
        assert result == (expected_prefix, expected_dict)
        mock_load_json.assert_called_once_with(expected_dict)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_utils_load_prefixed_json_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.output.utils.load_json_preserve_order_and_dupe_keys', autospec=True) as mock_load_json:
            data = '__XSSI_PREFIX__ {"name": "John", "age": 30, "city": "New York"}'
            expected_prefix = '__XSSI_PREFIX__'
            expected_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    
            result = load_prefixed_json(data)
    
>           assert result == (expected_prefix, expected_dict)
E           AssertionError: assert ('', <MagicMo...26583629904'>) == ('__XSSI_PREF...ame': 'John'})
E             
E             At index 0 diff: '' != '__XSSI_PREFIX__'
E             Use -v to get more diff

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_utils_load_prefixed_json_1_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_utils_load_prefixed_json_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.16s ===============================
"""