
import pytest
from httpie.cli.dicts import HTTPHeadersDict
from unittest.mock import patch

def test_invalid_key():
    headers = HTTPHeadersDict()
    
    with patch('httpie.cli.dicts.HTTPHeadersDict.popall', return_value=[]):
        with pytest.raises(KeyError):
            headers.remove_item('Invalid-Key', 'value')

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_1_test_invalid_key.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_invalid_key _______________________________

    def test_invalid_key():
        headers = HTTPHeadersDict()
    
        with patch('httpie.cli.dicts.HTTPHeadersDict.popall', return_value=[]):
            with pytest.raises(KeyError):
>               headers.remove_item('Invalid-Key', 'value')

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_1_test_invalid_key.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <HTTPHeadersDict()>, key = 'Invalid-Key', value = 'value'

    def remove_item(self, key, value):
        """
        Remove a (key, value) pair from the dict.
        """
        existing_values = self.popall(key)
>       existing_values.remove(value)
E       ValueError: list.remove(x): x not in list

httpie/httpie/cli/dicts.py:43: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_dicts_HTTPHeadersDict_remove_item_1_test_invalid_key.py::test_invalid_key
============================== 1 failed in 0.14s ===============================
"""