
from unittest.mock import patch
import pytest
from string_utils.generation import uuid  # Assuming the correct import path

@patch('string_utils.generation.uuid4')
def test_valid_input_default_format(mock_uuid4):
    mock_uuid4.return_value = "mocked_uuid"
    
    result_standard = uuid()
    assert isinstance(result_standard, str), "Expected a string representation of UUID"
    assert len(result_standard) == 36, "Expected standard UUID length to be 36 characters"
    
    result_hex = uuid(as_hex=True)
    assert isinstance(result_hex, str), "Expected a hex string representation of UUID"
    assert len(result_hex) == 32, "Expected hex UUID length to be 32 characters"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_valid_input_default_format.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_default_format ________________________

mock_uuid4 = <MagicMock name='uuid4' id='4335997024'>

    @patch('string_utils.generation.uuid4')
    def test_valid_input_default_format(mock_uuid4):
        mock_uuid4.return_value = "mocked_uuid"
    
        result_standard = uuid()
        assert isinstance(result_standard, str), "Expected a string representation of UUID"
>       assert len(result_standard) == 36, "Expected standard UUID length to be 36 characters"
E       AssertionError: Expected standard UUID length to be 36 characters
E       assert 11 == 36
E        +  where 11 = len('mocked_uuid')

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_valid_input_default_format.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_valid_input_default_format.py::test_valid_input_default_format
============================== 1 failed in 0.03s ===============================
"""