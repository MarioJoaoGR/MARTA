
import pytest
from inspect import signature
from isort.wrap_modes import _wrap_mode, _wrap_modes, _wrap_mode_interface

@pytest.mark.parametrize("function", [lambda: "test"])
def test_invalid_function_signature(function):
    with pytest.raises(TypeError):
        _wrap_mode(function)

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

isort/Test4DT_tests/test_isort_wrap_modes__wrap_mode_2_test_invalid_function_signature.py F [100%]

=================================== FAILURES ===================================
__________________ test_invalid_function_signature[<lambda>] ___________________

function = <function <lambda> at 0x7f117ae5f920>

    @pytest.mark.parametrize("function", [lambda: "test"])
    def test_invalid_function_signature(function):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_wrap_modes__wrap_mode_2_test_invalid_function_signature.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes__wrap_mode_2_test_invalid_function_signature.py::test_invalid_function_signature[<lambda>]
============================== 1 failed in 0.10s ===============================
"""