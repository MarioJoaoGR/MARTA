
import pytest
from pathlib import Path
from httpie.plugins.manager import _load_directories
from unittest.mock import patch, MagicMock
import sys

def test_invalid_input():
    with patch('httpie.plugins.manager._load_directories') as mock_load_directories:
        site_dirs = [Path('/path/to/site1'), Path('/path/to/site2')]
        for _ in _load_directories(site_dirs):
            pass
    
    # Assert that the function was called with the correct arguments
    mock_load_directories.assert_called_once_with(site_dirs)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with patch('httpie.plugins.manager._load_directories') as mock_load_directories:
            site_dirs = [Path('/path/to/site1'), Path('/path/to/site2')]
>           for _ in _load_directories(site_dirs):
E           TypeError: '_GeneratorContextManager' object is not iterable

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_1_test_invalid_input.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_manager__load_directories_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.21s ===============================
"""