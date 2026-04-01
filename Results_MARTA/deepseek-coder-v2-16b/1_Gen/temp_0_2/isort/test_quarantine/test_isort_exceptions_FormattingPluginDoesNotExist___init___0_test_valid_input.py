
import pytest
from isort.exceptions import FormattingPluginDoesNotExist

def test_valid_input():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        try:
            raise FormattingPluginDoesNotExist('valid_formatter')
        except FormattingPluginDoesNotExist as e:
            pass
    assert str(exc_info.value) == "Specified formatting plugin of valid_formatter does not exist."

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

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
E       Failed: DID NOT RAISE <class 'isort.exceptions.FormattingPluginDoesNotExist'>

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_valid_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""