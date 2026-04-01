
from isort.exceptions import FormattingPluginDoesNotExist
import pytest

def test_invalid_input():
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        formatter = None  # This should raise an exception since it's not a valid string input
        raise FormattingPluginDoesNotExist(formatter)
    
    assert str(excinfo.value) == "Specified formatting plugin of None does not exist."

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

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
            formatter = None  # This should raise an exception since it's not a valid string input
            raise FormattingPluginDoesNotExist(formatter)
    
>       assert str(excinfo.value) == "Specified formatting plugin of None does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 40 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___1_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""