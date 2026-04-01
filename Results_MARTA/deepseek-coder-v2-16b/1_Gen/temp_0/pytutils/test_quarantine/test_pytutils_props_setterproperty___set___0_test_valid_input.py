
from unittest.mock import MagicMock
import pytest
from pytutils.props import setterproperty

def test_valid_input():
    # Create a mock function to be used as the property func
    mock_func = MagicMock()
    
    # Define a class with the setterproperty applied to its value attribute
    class MyClass:
        def __init__(self, initial_value):
            self._value = initial_value
        
        @setterproperty
        def value(self, new_value):
            self._value = new_value
        
        def get_value(self):
            return self._value
    
    # Create an instance of MyClass
    obj = MyClass(10)
    
    # Test the initial value
    assert obj.get_value() == 10
    
    # Set a new value and check if it gets updated correctly
    obj.value = 20
    assert obj.get_value() == 20
    
    # Ensure that the mock function was called with the correct arguments
    mock_func.assert_called_with(obj, 20)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a mock function to be used as the property func
        mock_func = MagicMock()
    
        # Define a class with the setterproperty applied to its value attribute
        class MyClass:
            def __init__(self, initial_value):
                self._value = initial_value
    
            @setterproperty
            def value(self, new_value):
                self._value = new_value
    
            def get_value(self):
                return self._value
    
        # Create an instance of MyClass
        obj = MyClass(10)
    
        # Test the initial value
        assert obj.get_value() == 10
    
        # Set a new value and check if it gets updated correctly
        obj.value = 20
        assert obj.get_value() == 20
    
        # Ensure that the mock function was called with the correct arguments
>       mock_func.assert_called_with(obj, 20)

pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_valid_input.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock id='140203214817040'>
args = (<Test4DT_tests.test_pytutils_props_setterproperty___set___0_test_valid_input.test_valid_input.<locals>.MyClass object at 0x7f839ad0dc90>, 20)
kwargs = {}
expected = 'mock(<Test4DT_tests.test_pytutils_props_setterproperty___set___0_test_valid_input.test_valid_input.<locals>.MyClass object at 0x7f839ad0dc90>, 20)'
actual = 'not called.'
error_message = 'expected call not found.\nExpected: mock(<Test4DT_tests.test_pytutils_props_setterproperty___set___0_test_valid_input.test_valid_input.<locals>.MyClass object at 0x7f839ad0dc90>, 20)\n  Actual: not called.'

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\n  Actual: %s'
                    % (expected, actual))
>           raise AssertionError(error_message)
E           AssertionError: expected call not found.
E           Expected: mock(<Test4DT_tests.test_pytutils_props_setterproperty___set___0_test_valid_input.test_valid_input.<locals>.MyClass object at 0x7f839ad0dc90>, 20)
E             Actual: not called.

/usr/local/lib/python3.11/unittest/mock.py:930: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_props_setterproperty___set___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""