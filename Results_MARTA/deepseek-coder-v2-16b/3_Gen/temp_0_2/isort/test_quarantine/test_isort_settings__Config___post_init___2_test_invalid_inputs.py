
import pytest
from isort.settings import _Config, VALID_PY_TARGETS

def test_invalid_inputs():
    with pytest.raises(ValueError) as excinfo:
        config = _Config(py_version='4')
    assert str(excinfo.value) == f"The python version 4 is not supported. You can set a python version with the -py or --python-version flag. The following versions are supported: {', '.join([f'py{v}' for v in VALID_PY_TARGETS])}"

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

isort/Test4DT_tests/test_isort_settings__Config___post_init___2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError) as excinfo:
            config = _Config(py_version='4')
>       assert str(excinfo.value) == f"The python version 4 is not supported. You can set a python version with the -py or --python-version flag. The following versions are supported: {', '.join([f'py{v}' for v in VALID_PY_TARGETS])}"
E       assert "The python v..., '38', '39')" == 'The python v...7, py38, py39'
E         
E         Skipping 135 identical leading characters in diff, use -v to show
E         - upported: pyall, py2, py27, py3, py310, py311, py312, py313, py314, py36, py37, py38, py39
E         + upported: ('all', '2', '27', '3', '310', '311', '312', '313', '314', '36', '37', '38', '39')

isort/Test4DT_tests/test_isort_settings__Config___post_init___2_test_invalid_inputs.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__Config___post_init___2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.13s ===============================
"""