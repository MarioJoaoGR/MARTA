
import json
from unittest.mock import patch, MagicMock
from httpie.utils import load_json_preserve_order_and_dupe_keys

def test_valid_input():
    s = '{"name": "John", "age": 30, "city": "New York"}'
    with patch('httpie.utils.json.loads') as mock_loads:
        mock_instance = MagicMock()
        mock_instance.return_value = {'name': 'John', 'age': 30, 'city': 'New York'}
        mock_loads.return_value = mock_instance

        result = load_json_preserve_order_and_dupe_keys(s)

        assert result == {'name': 'John', 'age': 30, 'city': 'New York'}

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

httpie/Test4DT_tests_codestral/test_httpie_utils_load_json_preserve_order_and_dupe_keys_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        s = '{"name": "John", "age": 30, "city": "New York"}'
        with patch('httpie.utils.json.loads') as mock_loads:
            mock_instance = MagicMock()
            mock_instance.return_value = {'name': 'John', 'age': 30, 'city': 'New York'}
            mock_loads.return_value = mock_instance
    
            result = load_json_preserve_order_and_dupe_keys(s)
    
>           assert result == {'name': 'John', 'age': 30, 'city': 'New York'}
E           AssertionError: assert <MagicMock na...714926324944'> == {'age': 30, '...name': 'John'}
E             
E             Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_utils_load_json_preserve_order_and_dupe_keys_1_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_load_json_preserve_order_and_dupe_keys_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""