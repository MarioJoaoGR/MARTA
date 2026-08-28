
import pytest
from unittest.mock import patch
from py_backwards.utils.helpers import Settings, settings
import sys

def test_debug_with_enabled_settings():
    with patch('py_backwards.utils.helpers.settings', new=Settings(debug=True)):
        def get_debug_message():
            return "Debugging is enabled."
        
        from py_backwards.utils.helpers import debug
        debug(get_debug_message)
        captured = capsys.readouterr()
        assert "Debugging is enabled." in captured.err

def test_debug_with_disabled_settings():
    with patch('py_backwards.utils.helpers.settings', new=Settings(debug=False)):
        def get_debug_message():
            return "This should not be printed if debugging is disabled."
        
        from py_backwards.utils.helpers import debug
        debug(get_debug_message)
        captured = capsys.readouterr()
        assert captured.err == ""

def test_debug_with_lambda():
    with patch('py_backwards.utils.helpers.settings', new=Settings(debug=True)):
        from py_backwards.utils.helpers import debug
        debug(lambda: "This is a lambda debug message.")
        captured = capsys.readouterr()
        assert "This is a lambda debug message." in captured.err

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_________ ERROR collecting test_py_backwards_utils_helpers_debug_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_debug_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_debug_0.py:4: in <module>
    from py_backwards.utils.helpers import Settings, settings
E   ImportError: cannot import name 'Settings' from 'py_backwards.utils.helpers' (/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/helpers.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_debug_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""