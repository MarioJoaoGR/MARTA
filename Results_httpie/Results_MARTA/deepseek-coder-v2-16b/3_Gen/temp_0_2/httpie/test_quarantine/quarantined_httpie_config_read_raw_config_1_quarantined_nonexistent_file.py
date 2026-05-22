
import unittest.mock as mock
from pathlib import Path
from httpie.config import read_raw_config
from typing import Dict, Any
import json

def test_nonexistent_file():
    with mock.patch('httpie.config.open', side_effect=FileNotFoundError("File not found")):
        config = read_raw_config('settings', Path('non_existent_file.json'))
        assert config == {}

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_read_raw_config_1_test_nonexistent_file.py F [100%]

=================================== FAILURES ===================================
____________________________ test_nonexistent_file _____________________________

    def test_nonexistent_file():
        with mock.patch('httpie.config.open', side_effect=FileNotFoundError("File not found")):
            config = read_raw_config('settings', Path('non_existent_file.json'))
>           assert config == {}
E           assert None == {}

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_read_raw_config_1_test_nonexistent_file.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_read_raw_config_1_test_nonexistent_file.py::test_nonexistent_file
============================== 1 failed in 0.19s ===============================
"""