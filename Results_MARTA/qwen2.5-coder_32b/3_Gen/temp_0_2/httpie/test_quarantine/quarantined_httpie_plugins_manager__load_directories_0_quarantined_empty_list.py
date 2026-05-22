
import pytest
from pathlib import Path
from httpie.plugins.manager import _load_directories
import sys
import os
from unittest.mock import patch

def test_empty_list():
    site_dirs = []
    with patch('sys.path', [], create=True):  # Mock the sys.path to be empty initially
        loader = _load_directories(site_dirs)
        next(loader)  # Start the generator
        assert len(sys.path) == 0, "The Python path should not have any directories added."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_0_test_empty_list.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_empty_list ________________________________

    def test_empty_list():
        site_dirs = []
        with patch('sys.path', [], create=True):  # Mock the sys.path to be empty initially
            loader = _load_directories(site_dirs)
>           next(loader)  # Start the generator
E           TypeError: '_GeneratorContextManager' object is not an iterator

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_0_test_empty_list.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_0_test_empty_list.py::test_empty_list
============================== 1 failed in 0.16s ===============================
"""