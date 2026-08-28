
import pytest
from httpie.config import get_default_config_dir
from unittest.mock import patch, mock_open
import os
from pathlib import Path


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_get_default_config_dir_windows ______________________

    def test_get_default_config_dir_windows():
        with patch('httpie.config.is_windows', return_value=True):
            config_dir = get_default_config_dir()
            assert isinstance(config_dir, Path)
>           assert str(config_dir).endswith(os.path.expanduser('~') / 'AppData/Roaming/httpie')
E           TypeError: unsupported operand type(s) for /: 'str' and 'str'

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_0.py:12: TypeError
_______________________ test_get_default_config_dir_xdg ________________________

    def test_get_default_config_dir_xdg():
        with patch('os.environ', {'XDG_CONFIG_HOME': '/custom/xdg'}):
            home_dir = Path.home()
            xdg_config_dir = home_dir / 'xdg'
            if not xdg_config_dir.exists():
                xdg_config_dir.mkdir()
            config_dir = get_default_config_dir()
>           assert str(config_dir) == str(xdg_config_dir / 'httpie')
E           AssertionError: assert '/home/joaovitorino/.httpie' == '/home/joaovi...no/xdg/httpie'
E             
E             - /home/joaovitorino/xdg/httpie
E             ?                    ^^^^
E             + /home/joaovitorino/.httpie
E             ?                    ^

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_0.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_0.py::test_get_default_config_dir_windows
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_0.py::test_get_default_config_dir_xdg
============================== 2 failed in 0.11s ===============================
"""