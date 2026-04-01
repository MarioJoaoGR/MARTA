
from isort.place import _src_path
from unittest.mock import Mock
import pytest
from pathlib import Path

def test_valid_package():
    config = Mock()
    config.src_paths = [Path("/myproject/src")]
    assert _src_path("mypackage", config, src_paths=[Path("/myproject/src")]) == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')

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

isort/Test4DT_tests/test_isort_place__src_path_1_test_valid_package.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_package ______________________________

    def test_valid_package():
        config = Mock()
        config.src_paths = [Path("/myproject/src")]
>       assert _src_path("mypackage", config, src_paths=[Path("/myproject/src")]) == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')
E       AssertionError: assert None == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')
E        +  where None = _src_path('mypackage', <Mock id='140500119837776'>, src_paths=[PosixPath('/myproject/src')])

isort/Test4DT_tests/test_isort_place__src_path_1_test_valid_package.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__src_path_1_test_valid_package.py::test_valid_package
============================== 1 failed in 0.13s ===============================
"""