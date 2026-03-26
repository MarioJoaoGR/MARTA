
from unittest.mock import patch
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_input():
    with patch('string_utils.manipulation.__StringFormatter', autospec=True) as mock_formatter:
        # Arrange
        input_string = "valid string"
        
        # Act
        formatter = __StringFormatter(input_string)
        
        # Assert
        assert formatter.input_string == input_string
        mock_formatter.assert_called_once_with(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('string_utils.manipulation.__StringFormatter', autospec=True) as mock_formatter:
            # Arrange
            input_string = "valid string"
    
            # Act
            formatter = __StringFormatter(input_string)
    
            # Assert
            assert formatter.input_string == input_string
>           mock_formatter.assert_called_once_with(input_string)

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0_test_valid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='__StringFormatter' spec='__StringFormatter' id='4389333472'>
args = ('valid string',), kwargs = {}
msg = "Expected '__StringFormatter' to be called once. Called 0 times."

    def assert_called_once_with(self, /, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected '__StringFormatter' to be called once. Called 0 times.

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/unittest/mock.py:940: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___fix_saxon_genitive_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""