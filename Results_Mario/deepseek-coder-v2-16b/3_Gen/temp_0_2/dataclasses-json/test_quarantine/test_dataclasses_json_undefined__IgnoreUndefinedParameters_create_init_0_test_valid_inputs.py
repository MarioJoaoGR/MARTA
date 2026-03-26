
import pytest
from unittest.mock import patch, MagicMock
import inspect
import functools
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@pytest.fixture
def mock_class():
    return type('MockClass', (object,), {'__init__': lambda self, x, y: None})

def test_valid_inputs(mock_class):
    # Create an instance of the mock class
    obj = mock_class()
    
    # Use the _IgnoreUndefinedParameters to create a new initializer
    with patch('dataclasses_json.undefined._CatchAllUndefinedParameters', autospec=True) as mock_catchall:
        mock_catchall.return_value._separate_defined_undefined_kvs = MagicMock(return_value=(dict(), dict()))
        
        new_initializer = _IgnoreUndefinedParameters().create_init(obj)
        
        # Apply the new initializer to the instance
        obj.__init__ = new_initializer
        
        # Call the initializer with valid inputs
        obj.__init__(self=None, x='value1', y='value2')
        
        # Assert that the original init method was called with the correct parameters
        mock_catchall.return_value._separate_defined_undefined_kvs.assert_called_once_with(obj, {'x': 'value1', 'y': 'value2'})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

mock_class = <class 'Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_valid_inputs.MockClass'>

    def test_valid_inputs(mock_class):
        # Create an instance of the mock class
>       obj = mock_class()
E       TypeError: mock_class.<locals>.<lambda>() missing 2 required positional arguments: 'x' and 'y'

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_valid_inputs.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.04s ===============================
"""