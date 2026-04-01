
import pytest
from isort.exceptions import MissingSection

def test_missing_section():
    with pytest.raises(MissingSection) as excinfo:
        raise MissingSection("os", "standard library")
    
    assert str(excinfo.value) == "Found os import while parsing, but standard library was not included in the `sections` setting of your config. Please add it before continuing. See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."

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

isort/Test4DT_tests/test_isort_exceptions_MissingSection___init___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_missing_section _____________________________

    def test_missing_section():
        with pytest.raises(MissingSection) as excinfo:
            raise MissingSection("os", "standard library")
    
>       assert str(excinfo.value) == "Found os import while parsing, but standard library was not included in the `sections` setting of your config. Please add it before continuing. See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."
E       AssertionError: assert 'Found os imp...or more info.' == 'Found os imp...or more info.'
E         
E         Skipping 132 identical leading characters in diff, use -v to show
E         + continuing
E         - continuing. See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.
E         ? ------------
E         + See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.

isort/Test4DT_tests/test_isort_exceptions_MissingSection___init___0_test_edge_cases.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_MissingSection___init___0_test_edge_cases.py::test_missing_section
============================== 1 failed in 0.13s ===============================
"""