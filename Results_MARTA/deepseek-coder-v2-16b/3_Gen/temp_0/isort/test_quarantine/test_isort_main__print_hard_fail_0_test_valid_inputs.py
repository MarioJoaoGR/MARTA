
import pytest
from isort.main import _print_hard_fail  # Correctly importing the function
from unittest.mock import patch, MagicMock  # Importing necessary modules for mocking

@pytest.fixture(autouse=True)
def mock_config():
    config = MagicMock()
    yield config

@patch('isort.main._print_hard_fail')
def test_valid_inputs(_print_hard_fail_mock):
    # Arrange
    config = mock_config()  # Using the fixture to provide a mocked Config object
    
    # Act
    _print_hard_fail(config)  # Calling the function with the mocked Config
    
    # Assert
    _print_hard_fail_mock.assert_called_once_with(
        config, None, "Unrecoverable exception thrown when parsing ! "
                      "This should NEVER happen.\n"
                      "If encountered, please open an issue: https://github.com/PyCQA/isort/issues/new"
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_main__print_hard_fail_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________
Fixture "mock_config" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__print_hard_fail_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""