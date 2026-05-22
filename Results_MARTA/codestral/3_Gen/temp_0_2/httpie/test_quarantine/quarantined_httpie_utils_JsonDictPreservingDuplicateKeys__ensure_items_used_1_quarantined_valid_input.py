
import sys
from unittest import TestCase, mock
from httpie.utils import JsonDictPreservingDuplicateKeys

class TestJsonDictPreservingDuplicateKeys(TestCase):
    def test_valid_input(self):
        items = {'key1': 'value1', 'key2': 'value2'}
        json_dict = JsonDictPreservingDuplicateKeys(items)
        expected_output = {'__hack__': '__hack__', 'key1': 'value1', 'key2': 'value2'}
        self.assertEqual(json_dict, expected_output)

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

httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_____________ TestJsonDictPreservingDuplicateKeys.test_valid_input _____________

self = <Test4DT_tests_codestral.test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_1_test_valid_input.TestJsonDictPreservingDuplicateKeys testMethod=test_valid_input>

    def test_valid_input(self):
        items = {'key1': 'value1', 'key2': 'value2'}
        json_dict = JsonDictPreservingDuplicateKeys(items)
        expected_output = {'__hack__': '__hack__', 'key1': 'value1', 'key2': 'value2'}
>       self.assertEqual(json_dict, expected_output)
E       AssertionError: JsonDictPreservingDuplicateKeys(['key1', 'key2']) != {'__hack__': '__hack__', 'key1': 'value1', 'key2': 'value2'}

httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_1_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_1_test_valid_input.py::TestJsonDictPreservingDuplicateKeys::test_valid_input
============================== 1 failed in 0.18s ===============================
"""