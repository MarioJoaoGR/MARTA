
import json
from unittest.mock import patch, MagicMock
import pytest

def json_encode(value: Any) -> str:
    """JSON-encodes the given Python object."""
    # JSON permits but does not require forward slashes to be escaped.
    # This is useful when json data is emitted in a <script> tag
    # in HTML, as it prevents </script> tags from prematurely terminating
    # the JavaScript.  Some json libraries do this escaping by default,
    # although python's standard library does not, so we do it here.
    # http://stackoverflow.com/questions/1580647/json-why-are-forward-slashes-escaped
    return json.dumps(value).replace("</", "<\\/")

# Test cases for json_encode function
def test_json_encode_dictionary():
    obj = {"key": "value", "script": "<script>alert('danger!');</script>"}
    encoded_obj = json_encode(obj)
    assert isinstance(encoded_obj, str), "Encoded object should be a string"
    assert encoded_obj == '{"key": "value", "script": "<script>alert(\'danger!\');\\/script>"}', f"Expected: {{'key': 'value', 'script': '<script>alert(\'danger!\');\\/script>'}} Got: {encoded_obj}"

def test_json_encode_list():
    data_list = [1, 2, 3]
    encoded_list = json_encode(data_list)
    assert isinstance(encoded_list, str), "Encoded list should be a string"
    assert encoded_list == '[1, 2, 3]', f"Expected: '[1, 2, 3]' Got: {encoded_list}"

def test_json_encode_string():
    data_string = "This is a test string with <script>alert('danger!');</script>"
    encoded_string = json_encode(data_string)
    assert isinstance(encoded_string, str), "Encoded string should be a string"
    assert encoded_string == 'This is a test string with \\u003cscript\\u003ealert(\'danger!\');\\u003c/script\\u003e', f"Expected: 'This is a test string with \\u003cscript\\u003ealert(\'danger!\');\\u003c/script\\u003e' Got: {encoded_string}"

def test_json_encode_integer():
    data_int = 123
    encoded_int = json_encode(data_int)
    assert isinstance(encoded_int, str), "Encoded integer should be a string"
    assert encoded_int == '123', f"Expected: '123' Got: {encoded_int}"

def test_json_encode_float():
    data_float = 123.45
    encoded_float = json_encode(data_float)
    assert isinstance(encoded_float, str), "Encoded float should be a string"
    assert encoded_float == '123.45', f"Expected: '123.45' Got: {encoded_float}"

def test_json_encode_complex_structure():
    complex_data = {"num": 1, "str": "example", "nested": {"key": "value"}}
    encoded_complex = json_encode(complex_data)
    assert isinstance(encoded_complex, str), "Encoded complex structure should be a string"
    assert encoded_complex == '{"num": 1, "str": "example", "nested": {"key": "value"}}', f"Expected: {{'num': 1, 'str': 'example', 'nested': {{'key': 'value'}}}} Got: {encoded_complex}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting test_tornado_escape_json_encode_0.py _____________
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_json_encode_0.py:6: in <module>
    def json_encode(value: Any) -> str:
E   NameError: name 'Any' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_json_encode_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""