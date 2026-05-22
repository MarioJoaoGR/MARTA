
import json
from httpie.utils import load_json_preserve_order_and_dupe_keys, JsonDictPreservingDuplicateKeys

def test_invalid_input():
    s = '{"name": "John", "age": 30, "city": "New York"}'
    result = load_json_preserve_order_and_dupe_keys(s)
    assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
    assert len(result) == 3, f"Expected 3 key-value pairs but found {len(result)}"

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_load_json_preserve_order_and_dupe_keys_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        s = '{"name": "John", "age": 30, "city": "New York"}'
        result = load_json_preserve_order_and_dupe_keys(s)
        assert isinstance(result, dict), f"Expected a dictionary but got {type(result)}"
>       assert len(result) == 3, f"Expected 3 key-value pairs but found {len(result)}"
E       AssertionError: Expected 3 key-value pairs but found 1
E       assert 1 == 3
E        +  where 1 = len(JsonDictPreservingDuplicateKeys([('name', 'John'), ('age', 30), ('city', 'New York')]))

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_load_json_preserve_order_and_dupe_keys_1_test_invalid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_load_json_preserve_order_and_dupe_keys_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.13s ===============================
"""