
import pytest
from isort.exceptions import ProfileDoesNotExist

def test_empty_string_input():
    profile = ''
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        raise ProfileDoesNotExist(profile)
    assert str(excinfo.value) == "Specified profile of  does not exist. Available profiles: ."

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

isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_empty_string_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_empty_string_input ____________________________

    def test_empty_string_input():
        profile = ''
        with pytest.raises(ProfileDoesNotExist) as excinfo:
            raise ProfileDoesNotExist(profile)
>       assert str(excinfo.value) == "Specified profile of  does not exist. Available profiles: ."
E       AssertionError: assert 'Specified pr...ake,appnexus.' == 'Specified pr...e profiles: .'
E         
E         Skipping 48 identical leading characters in diff, use -v to show
E         - profiles: .
E         + profiles: black,django,pycharm,google,open_stack,plone,attrs,hug,wemake,appnexus.

isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_empty_string_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_empty_string_input.py::test_empty_string_input
============================== 1 failed in 0.10s ===============================
"""