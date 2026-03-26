
import pytest
from isort.exceptions import UnsupportedSettings

def test_valid_input():
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings({"unsupported_setting": {"value": "some_value", "source": "CLI"}})
    
    assert str(excinfo.value) == (
        "isort was provided settings that it doesn't support:\n\n"
        "unsupported_setting: {'value': 'some_value', 'source': 'CLI'}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options."
    )

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

isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with pytest.raises(UnsupportedSettings) as excinfo:
            raise UnsupportedSettings({"unsupported_setting": {"value": "some_value", "source": "CLI"}})
    
>       assert str(excinfo.value) == (
            "isort was provided settings that it doesn't support:\n\n"
            "unsupported_setting: {'value': 'some_value', 'source': 'CLI'}\n\n"
            "For a complete and up-to-date listing of supported settings see: "
            "https://pycqa.github.io/isort/docs/configuration/options."
        )
E       AssertionError: assert 'isort was pr...on/options.\n' == 'isort was pr...tion/options.'
E         
E         Skipping 44 identical leading characters in diff, use -v to show
E           support:
E           
E         - unsupported_setting: {'value': 'some_value', 'source': 'CLI'}
E         + 	- unsupported_setting = some_value  (source: 'CLI')
E           ...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings___init___0_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""