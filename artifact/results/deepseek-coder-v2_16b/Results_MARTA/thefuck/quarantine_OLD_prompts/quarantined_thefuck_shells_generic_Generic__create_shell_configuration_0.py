
import pytest
from unittest.mock import patch, MagicMock
from thefuck.shells.generic import Generic
from thefuck.types import ShellConfiguration
from pathlib import Path

# Test for creating a shell configuration with valid content and path
def test_create_shell_configuration_valid():
    generic = Generic()
    with patch('thefuck.types.Path.expanduser', return_value=MagicMock(exists=lambda: True)):
        config = generic._create_shell_configuration('export PATH=$HOME/bin:$PATH', '/home/user/shell_config.sh', True)
        assert isinstance(config, ShellConfiguration)
        assert config.content == 'export PATH=$HOME/bin:$PATH'
        assert config.path == '/home/user/shell_config.sh'
        assert config.reload is True
        assert config.can_configure_automatically is True

# Test for creating a shell configuration with invalid content and path
def test_create_shell_configuration_invalid():
    generic = Generic()
    with patch('thefuck.types.Path.expanduser', return_value=MagicMock(exists=lambda: False)):
        config = generic._create_shell_configuration('export PATH=$HOME/bin:$PATH', '/home/user/shell_config.sh', True)
        assert isinstance(config, ShellConfiguration)
        assert config.content == 'export PATH=$HOME/bin:$PATH'
        assert config.path == '/home/user/shell_config.sh'
        assert config.reload is True
        assert config.can_configure_automatically is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_thefuck_shells_generic_Generic__create_shell_configuration_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_shells_generic_Generic__create_shell_configuration_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_shells_generic_Generic__create_shell_configuration_0.py:5: in <module>
    from thefuck.types import ShellConfiguration
E   ImportError: cannot import name 'ShellConfiguration' from 'thefuck.types' (/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py)
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_shells_generic_Generic__create_shell_configuration_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.24s ==========================
"""