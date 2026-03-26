
import pytest
from setuptools import setup
from isort.setuptools_commands import ISortCommand

@pytest.fixture
def dist():
    return setup(name='test_package', packages=['test_module'])

def test_valid_inputs(dist):
    command = ISortCommand()
    command.distribution = dist
    command.run()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_setuptools_commands_ISortCommand_run_0_test_valid_inputs
isort/Test4DT_tests/test_isort_setuptools_commands_ISortCommand_run_0_test_valid_inputs.py:11:14: E1120: No value for argument 'dist' in constructor call (no-value-for-parameter)


"""