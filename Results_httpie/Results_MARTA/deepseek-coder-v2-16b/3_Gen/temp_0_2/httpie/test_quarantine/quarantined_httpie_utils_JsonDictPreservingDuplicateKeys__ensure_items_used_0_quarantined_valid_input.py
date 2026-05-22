
import sys
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys, Items
import unittest
from unittest.mock import patch

class TestJsonDictPreservingDuplicateKeys(unittest.TestCase):
    def test_valid_input(self):
        items = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
        
        with patch('httpie.utils.sys') as mock_sys:
            mock_sys.version_info = (3, 8)  # Mocking sys.version_info to simulate >= 3.8
            
            json_dict = JsonDictPreservingDuplicateKeys(items)
            
            self.assertEqual(json_dict['__hack__'], '__hack__')
            self.assertIn('key1', json_dict)
            self.assertIn('key2', json_dict)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_____________ TestJsonDictPreservingDuplicateKeys.test_valid_input _____________

self = <test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_0_test_valid_input.TestJsonDictPreservingDuplicateKeys testMethod=test_valid_input>

    def test_valid_input(self):
        items = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
    
        with patch('httpie.utils.sys') as mock_sys:
            mock_sys.version_info = (3, 8)  # Mocking sys.version_info to simulate >= 3.8
    
            json_dict = JsonDictPreservingDuplicateKeys(items)
    
            self.assertEqual(json_dict['__hack__'], '__hack__')
>           self.assertIn('key1', json_dict)
E           AssertionError: 'key1' not found in JsonDictPreservingDuplicateKeys(['key1', 'key2'])

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_0_test_valid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_0_test_valid_input.py::TestJsonDictPreservingDuplicateKeys::test_valid_input
============================== 1 failed in 0.20s ===============================
"""