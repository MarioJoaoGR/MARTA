
import pytest
from dataclasses_json.undefined import UndefinedParameterError
from unittest.mock import patch, MagicMock

# Assuming _RaiseUndefinedParameters is defined in the same file or module
with patch('dataclasses_json.undefined._RaiseUndefinedParameters') as mock_raise_undefined:
    # Create a mock instance of _RaiseUndefinedParameters for testing
    mock_instance = mock_raise_undefined.return_value
    
    def test_handle_from_dict():
        # Define the dictionary with known and unknown parameters
        kvs = {'param1': 1, 'extra_param': 2}
        
        # Call the method under test
        result = mock_instance.handle_from_dict(kvs=kvs)
        
        # Assert that only known parameters are returned and no error is raised
        assert result == {'param1': 1}
    
    test_handle_from_dict()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases.py _
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases.py:21: in <module>
    test_handle_from_dict()
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases.py:19: in test_handle_from_dict
    assert result == {'param1': 1}
E   AssertionError: assert <MagicMock name='_RaiseUndefinedParameters().handle_from_dict()' id='4371179856'> == {'param1': 1}
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__RaiseUndefinedParameters_handle_from_dict_0_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.07s ===============================
"""