
import pytest
from pathlib import Path
from httpie.config import read_raw_config, ConfigFileError
from unittest.mock import patch

def test_none_input():
    config_type = 'test'
    path = Path('nonexistent_file.json')
    
    with patch('builtins.open', side_effect=FileNotFoundError()):
        with pytest.raises(ConfigFileError) as excinfo:
            read_raw_config(config_type, path)
        
        assert str(excinfo.value) == "cannot read test file: [Errno 2] No such file or directory: 'nonexistent_file.json'"

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_read_raw_config_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        config_type = 'test'
        path = Path('nonexistent_file.json')
    
        with patch('builtins.open', side_effect=FileNotFoundError()):
>           with pytest.raises(ConfigFileError) as excinfo:
E           Failed: DID NOT RAISE <class 'httpie.config.ConfigFileError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_read_raw_config_1_test_none_input.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_read_raw_config_1_test_none_input.py::test_none_input
============================== 1 failed in 0.15s ===============================
"""