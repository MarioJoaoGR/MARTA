
import pytest
from unittest.mock import patch
from materialize_headers import materialize_headers

def test_valid_input():
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}
    expected_output = [
        {'name': 'Content-Type', 'value': 'application/json'},
        {'name': 'Authorization', 'value': 'Bearer token'}
    ]
    
    with patch('materialize_headers.copy') as mock_copy:
        mock_copy.return_value = headers
        result = materialize_headers(headers)
        
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_sessions_materialize_headers_3_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_sessions_materialize_headers_3_test_valid_input.py:4:0: E0401: Unable to import 'materialize_headers' (import-error)


"""