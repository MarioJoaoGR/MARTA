
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_empty_string_input():
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist("")
    assert str(excinfo.value) == "Specified formatting plugin of  does not exist."

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

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_empty_string_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_empty_string_input ____________________________

    def test_empty_string_input():
        with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
            raise FormattingPluginDoesNotExist("")
>       assert str(excinfo.value) == "Specified formatting plugin of  does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 36 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_empty_string_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_empty_string_input.py::test_empty_string_input
============================== 1 failed in 0.13s ===============================
"""