
import json
from unittest.mock import patch
from pytest import raises
from tornado.escape import to_basestring

def json_decode(value: Union[str, bytes]) -> Any:
    """Returns Python objects for the given JSON string.

    Supports both `str` and `bytes` inputs.
    """
    return json.loads(to_basestring(value))

# Test cases
def test_valid_input_string():
    valid_json = '{"key": "value"}'
    with patch('tornado.escape.to_basestring', return_value=valid_json):
        result = json_decode(valid_json)
        assert result == {"key": "value"}

def test_valid_input_bytes():
    byte_data = b'{"key": "value"}'
    with patch('tornado.escape.to_basestring', return_value=byte_data):
        with raises(UnicodeDecodeError):
            json_decode(byte_data)

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
____________ ERROR collecting test_tornado_escape_json_decode_0.py _____________
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_json_decode_0.py:7: in <module>
    def json_decode(value: Union[str, bytes]) -> Any:
E   NameError: name 'Union' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_escape_json_decode_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""