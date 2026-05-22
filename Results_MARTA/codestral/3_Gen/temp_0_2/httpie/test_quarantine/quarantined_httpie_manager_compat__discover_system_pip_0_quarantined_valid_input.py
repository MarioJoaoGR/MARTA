
from httpie.manager.compat import _discover_system_pip
from unittest.mock import patch, MagicMock
import subprocess
from contextlib import suppress

def test_valid_input():
    with patch('shutil.which', return_value='/usr/local/bin/pip3'):
        mock_check_output = MagicMock()
        mock_check_output.return_value.stdout = "pip 21.0.1 from /usr/local/lib/python3.8/site-packages (python 3.8)"
        
        with patch('subprocess.check_output', mock_check_output):
            result = _discover_system_pip()
            
            assert result == '/usr/local/bin/pip3'

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

httpie/Test4DT_tests_codestral/test_httpie_manager_compat__discover_system_pip_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('shutil.which', return_value='/usr/local/bin/pip3'):
            mock_check_output = MagicMock()
            mock_check_output.return_value.stdout = "pip 21.0.1 from /usr/local/lib/python3.8/site-packages (python 3.8)"
    
            with patch('subprocess.check_output', mock_check_output):
>               result = _discover_system_pip()

httpie/Test4DT_tests_codestral/test_httpie_manager_compat__discover_system_pip_0_test_valid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def _discover_system_pip() -> List[str]:
        # When we are running inside of a frozen binary, we need the system
        # pip to install plugins since there is no way for us to execute any
        # code outside of the HTTPie.
        #
        # We explicitly depend on system pip, so the SystemError should not
        # be executed (except for broken installations).
        def _check_pip_version(pip_location: Optional[str]) -> bool:
            if not pip_location:
                return False
    
            with suppress(subprocess.CalledProcessError):
                stdout = subprocess.check_output([pip_location, "--version"], text=True)
                return "python 3" in stdout
    
        targets = [
            "pip",
            "pip3"
        ]
        for target in targets:
            pip_location = shutil.which(target)
            if _check_pip_version(pip_location):
                return pip_location
    
>       raise SystemError("Couldn't find 'pip' executable. Please ensure that pip in your system is available.")
E       SystemError: Couldn't find 'pip' executable. Please ensure that pip in your system is available.

httpie/httpie/manager/compat.py:42: SystemError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_compat__discover_system_pip_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""