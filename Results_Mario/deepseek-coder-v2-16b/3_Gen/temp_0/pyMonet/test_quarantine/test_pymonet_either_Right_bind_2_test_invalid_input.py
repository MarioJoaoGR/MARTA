
from pymonet.either import Right, Left  # Import Right and Left from pymonet.either
import pytest
from unittest.mock import patch

def test_invalid_input():
    right_instance = Right(42)  # Create an instance of Right with a value of 42

    # Mock the print function to check if it is called correctly
    with patch('builtins.print') as mocked_print:
        # Call the bind method which should call the mapper function internally
        right_instance.bind(lambda x: x * 2)  # Apply the mapper function (doubling the value) to the stored value

        # Check if the print function was called correctly, which means bind method worked as expected.
        mocked_print.assert_called_with(84)  # Expected output is 84 after doubling the value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        right_instance = Right(42)  # Create an instance of Right with a value of 42
    
        # Mock the print function to check if it is called correctly
        with patch('builtins.print') as mocked_print:
            # Call the bind method which should call the mapper function internally
            right_instance.bind(lambda x: x * 2)  # Apply the mapper function (doubling the value) to the stored value
    
            # Check if the print function was called correctly, which means bind method worked as expected.
>           mocked_print.assert_called_with(84)  # Expected output is 84 after doubling the value

pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_2_test_invalid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='print' id='140245395342800'>, args = (84,), kwargs = {}
expected = 'print(84)', actual = 'not called.'
error_message = 'expected call not found.\nExpected: print(84)\n  Actual: not called.'

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
E           Expected: print(84)
E             Actual: not called.

/usr/local/lib/python3.11/unittest/mock.py:930: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""