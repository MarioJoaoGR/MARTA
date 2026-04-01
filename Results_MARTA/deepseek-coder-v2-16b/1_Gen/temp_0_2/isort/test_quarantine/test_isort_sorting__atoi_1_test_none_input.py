
from isort.sorting import _atoi
import pytest

def test_none_input():
    with pytest.raises(TypeError):
        assert _atoi(None) is None

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

isort/Test4DT_tests/test_isort_sorting__atoi_1_test_none_input.py F      [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
>           assert _atoi(None) is None

isort/Test4DT_tests/test_isort_sorting__atoi_1_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = None

    def _atoi(text: str) -> Any:
>       return int(text) if text.isdigit() else text
E       AttributeError: 'NoneType' object has no attribute 'isdigit'

isort/isort/sorting.py:127: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting__atoi_1_test_none_input.py::test_none_input
============================== 1 failed in 0.10s ===============================
"""