
import pytest
from unittest.mock import patch, Mock
from httpie.manager.compat import run_pip

def test_invalid_command():
    with patch('httpie.manager.compat.subprocess.run') as mock_run:
        # Configure the mock to return an error code and output
        mock_run.return_value = Mock(returncode=1, stdout=b'', stderr=b'Error message')
        
        with pytest.raises(RuntimeError) as excinfo:
            run_pip(['invalid', 'command'])
        
        assert str(excinfo.value) == "Pip command failed with output:\nError message"

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_1_test_invalid_command.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_command _____________________________

    def test_invalid_command():
        with patch('httpie.manager.compat.subprocess.run') as mock_run:
            # Configure the mock to return an error code and output
            mock_run.return_value = Mock(returncode=1, stdout=b'', stderr=b'Error message')
    
>           with pytest.raises(RuntimeError) as excinfo:
E           Failed: DID NOT RAISE <class 'RuntimeError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_1_test_invalid_command.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_1_test_invalid_command.py::test_invalid_command
============================== 1 failed in 0.10s ===============================
"""