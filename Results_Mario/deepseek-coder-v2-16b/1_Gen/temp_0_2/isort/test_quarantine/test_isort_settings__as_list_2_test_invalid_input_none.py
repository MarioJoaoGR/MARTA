
import pytest
from isort.settings import _as_list

def test_invalid_input_none():
    with pytest.raises(TypeError):
        _as_list(None)

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

isort/Test4DT_tests/test_isort_settings__as_list_2_test_invalid_input_none.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        with pytest.raises(TypeError):
>           _as_list(None)

isort/Test4DT_tests/test_isort_settings__as_list_2_test_invalid_input_none.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def _as_list(value: str) -> list[str]:
        if isinstance(value, list):
            return [item.strip() for item in value]
>       filtered = [item.strip() for item in value.replace("\n", ",").split(",") if item.strip()]
E       AttributeError: 'NoneType' object has no attribute 'replace'

isort/isort/settings.py:738: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__as_list_2_test_invalid_input_none.py::test_invalid_input_none
============================== 1 failed in 0.12s ===============================
"""