
import pytest
from isort._vendored.tomli._parser import Flags

def test_invalid_flag():
    flags = Flags()
    with pytest.raises(KeyError):  # Assuming the expected error is KeyError for a non-existent flag
        assert flags.is_(["non_existent_key"], 1)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__1_test_invalid_flag.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_flag _______________________________

    def test_invalid_flag():
        flags = Flags()
        with pytest.raises(KeyError):  # Assuming the expected error is KeyError for a non-existent flag
>           assert flags.is_(["non_existent_key"], 1)
E           AssertionError: assert False
E            +  where False = is_(['non_existent_key'], 1)
E            +    where is_ = <isort._vendored.tomli._parser.Flags object at 0x7f17f287bdd0>.is_

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__1_test_invalid_flag.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__1_test_invalid_flag.py::test_invalid_flag
============================== 1 failed in 0.12s ===============================
"""