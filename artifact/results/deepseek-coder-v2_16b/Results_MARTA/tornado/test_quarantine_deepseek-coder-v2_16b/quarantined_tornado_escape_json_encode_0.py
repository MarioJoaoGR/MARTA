
import pytest
from tornado import escape
import json

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_json_encode_0.py F [100%]

=================================== FAILURES ===================================
____________________________ test_json_encode_basic ____________________________

    def test_json_encode_basic():
        # Define a sample dictionary with special characters in the script key
        obj = {"key": "value", "script": "<script>alert('danger!');</script>"}
    
        # Call the json_encode function with the sample object
        encoded_obj = escape.json_encode(obj)
    
        # Define the expected output after encoding and escaping forward slashes
        expected_output = '{"key": "value", "script": "<script>alert(\'danger!\');\\/script>"}'
    
        # Assert that the encoded object matches the expected output
>       assert encoded_obj == expected_output, f"Expected {expected_output}, but got {encoded_obj}"
E       AssertionError: Expected {"key": "value", "script": "<script>alert('danger!');\/script>"}, but got {"key": "value", "script": "<script>alert('danger!');<\/script>"}
E       assert '{"key": "val...<\\/script>"}' == '{"key": "val...;\\/script>"}'
E         
E         Skipping 43 identical leading characters in diff, use -v to show
E         - danger!');\/script>"}
E         + danger!');<\/script>"}
E         ?           +

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_json_encode_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_json_encode_0.py::test_json_encode_basic
============================== 1 failed in 0.07s ===============================
"""