
from unittest.mock import patch
from string_utils.generation import uuid
import pytest

def test_valid_input_default_format():
    with patch('string_utils.generation.uuid4') as mock_uuid4:
        # Mocking the return value of uuid4()
        mock_uuid4.return_value = "mocked_uuid"

        # Test default format (non-hex)
        result = uuid()
        assert isinstance(result, str), "Expected a string representation of UUID."
        assert len(result) == 36, "Expected the length to be 36 characters for standard UUID format."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_default_format.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_default_format ________________________

    def test_valid_input_default_format():
        with patch('string_utils.generation.uuid4') as mock_uuid4:
            # Mocking the return value of uuid4()
            mock_uuid4.return_value = "mocked_uuid"
    
            # Test default format (non-hex)
            result = uuid()
            assert isinstance(result, str), "Expected a string representation of UUID."
>           assert len(result) == 36, "Expected the length to be 36 characters for standard UUID format."
E           AssertionError: Expected the length to be 36 characters for standard UUID format.
E           assert 11 == 36
E            +  where 11 = len('mocked_uuid')

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_default_format.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_default_format.py::test_valid_input_default_format
============================== 1 failed in 0.02s ===============================
"""