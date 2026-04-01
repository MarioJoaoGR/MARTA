
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_none_input():
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        try:
            raise FormattingPluginDoesNotExist(None)
        except FormattingPluginDoesNotExist as e:
            assert e.formatter is None, "The formatter should be set to None"
            raise
    
    # The error message should indicate the formatter was None
    assert str(excinfo.value) == "Specified formatting plugin of None does not exist.", "Error message should indicate the formatter was None"

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

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
            try:
                raise FormattingPluginDoesNotExist(None)
            except FormattingPluginDoesNotExist as e:
                assert e.formatter is None, "The formatter should be set to None"
                raise
    
        # The error message should indicate the formatter was None
>       assert str(excinfo.value) == "Specified formatting plugin of None does not exist.", "Error message should indicate the formatter was None"
E       AssertionError: Error message should indicate the formatter was None
E       assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 40 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_none_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_none_input.py::test_none_input
============================== 1 failed in 0.10s ===============================
"""