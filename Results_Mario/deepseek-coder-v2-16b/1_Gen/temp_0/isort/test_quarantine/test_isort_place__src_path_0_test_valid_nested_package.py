
from isort.place import _src_path
from unittest.mock import Mock
import pytest
from pathlib import Path

def test_valid_nested_package():
    config = Mock()
    config.src_paths = [Path("/myproject/src")]
    config.namespace_packages = set()
    config.auto_identify_namespace_packages = False
    config.supported_extensions = ('.py', '.pyi')
    
    result = _src_path("subpackage.mymodule", config, src_paths=[Path("/myproject/src")])
    assert result == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')

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

isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_nested_package.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_nested_package ___________________________

    def test_valid_nested_package():
        config = Mock()
        config.src_paths = [Path("/myproject/src")]
        config.namespace_packages = set()
        config.auto_identify_namespace_packages = False
        config.supported_extensions = ('.py', '.pyi')
    
        result = _src_path("subpackage.mymodule", config, src_paths=[Path("/myproject/src")])
>       assert result == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')
E       AssertionError: assert None == ('FIRSTPARTY', 'Found in one of the configured src_paths: /myproject/src.')

isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_nested_package.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__src_path_0_test_valid_nested_package.py::test_valid_nested_package
============================== 1 failed in 0.10s ===============================
"""