
from isort._vendored.tomli._parser import Flags
import pytest

def test_none_input():
    flags = Flags()
    with pytest.raises(KeyError):
        assert flags.unset_all(["non_existent_key"])

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_5_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        flags = Flags()
        with pytest.raises(KeyError):
>           assert flags.unset_all(["non_existent_key"])
E           AssertionError: assert None
E            +  where None = unset_all(['non_existent_key'])
E            +    where unset_all = <isort._vendored.tomli._parser.Flags object at 0x7f6ac236bd90>.unset_all

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_5_test_none_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_5_test_none_input.py::test_none_input
============================== 1 failed in 0.13s ===============================
"""