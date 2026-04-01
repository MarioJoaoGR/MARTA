
import argparse
import pytest
from isort.main import _build_arg_parser

def test_build_arg_parser_none_inputs():
    # Test with None input
    with pytest.raises(SystemExit):
        _build_arg_parser()

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

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________ test_build_arg_parser_none_inputs _______________________

    def test_build_arg_parser_none_inputs():
        # Test with None input
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_edge_cases.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_edge_cases.py::test_build_arg_parser_none_inputs
============================== 1 failed in 0.10s ===============================
"""