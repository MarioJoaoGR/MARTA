
import argparse
import sys
from unittest import mock
import pytest
from isort.main import _build_arg_parser

def test_none_value():
    with pytest.raises(SystemExit):
        try:
            _build_arg_parser()
        except SystemExit as e:
            assert e.code == 0

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

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_value ________________________________

    def test_none_value():
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_edge_case.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_edge_case.py::test_none_value
============================== 1 failed in 0.11s ===============================
"""