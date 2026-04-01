
import pytest
from isort.exceptions import UnsupportedSettings

def test_edge_case():
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings({"settings_name": {"value": "some_value", "source": "CLI"}})
    
    assert str(exc_info.value) == (
        "isort was provided settings that it doesn't support:\n\n"
        "- settings_name = some_value  (source: 'CLI')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options.\n"
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

isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings___init___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with pytest.raises(UnsupportedSettings) as exc_info:
            raise UnsupportedSettings({"settings_name": {"value": "some_value", "source": "CLI"}})
    
>       assert str(exc_info.value) == (
            "isort was provided settings that it doesn't support:\n\n"
            "- settings_name = some_value  (source: 'CLI')\n\n"
            "For a complete and up-to-date listing of supported settings see: "
            "https://pycqa.github.io/isort/docs/configuration/options.\n"
        )
E       AssertionError: assert 'isort was pr...on/options.\n' == 'isort was pr...on/options.\n'
E         
E         Skipping 44 identical leading characters in diff, use -v to show
E           support:
E           
E         - - settings_name = some_value  (source: 'CLI')
E         + 	- settings_name = some_value  (source: 'CLI')
E         ? +
E           
E           For a complete and up-to-date listing of supported settings see: https://pycqa.github.io/isort/docs/configuration/options.

isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings___init___0_test_edge_case.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_UnsupportedSettings___init___0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.11s ===============================
"""