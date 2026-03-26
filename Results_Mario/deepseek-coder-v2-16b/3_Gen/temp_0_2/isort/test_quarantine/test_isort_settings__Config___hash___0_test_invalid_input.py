
import pytest
from isort.settings import _Config

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        _Config(py_version='4')
    assert str(excinfo.value) == "Invalid py_version value '4'. Expected one of ['2', '3']"

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

isort/Test4DT_tests/test_isort_settings__Config___hash___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError) as excinfo:
            _Config(py_version='4')
>       assert str(excinfo.value) == "Invalid py_version value '4'. Expected one of ['2', '3']"
E       assert "The python v..., '38', '39')" == "Invalid py_v...of ['2', '3']"
E         
E         - Invalid py_version value '4'. Expected one of ['2', '3']
E         + The python version 4 is not supported. You can set a python version with the -py or --python-version flag. The following versions are supported: ('all', '2', '27', '3', '310', '311', '312', '313', '314', '36', '37', '38', '39')

isort/Test4DT_tests/test_isort_settings__Config___hash___0_test_invalid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__Config___hash___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""