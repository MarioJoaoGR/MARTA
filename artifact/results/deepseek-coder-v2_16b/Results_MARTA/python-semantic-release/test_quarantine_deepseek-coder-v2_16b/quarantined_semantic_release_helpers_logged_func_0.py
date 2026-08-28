
import pytest
from semantic_release.helpers import logged_func
import logging

# Set up a logger for testing
logger = logging.getLogger(__name__)
logged_function = logged_func(logger)

def test_logged_func_class_method():
    class MyClass:
        def __init__(self):
            self.logger = logger
        
        @logged_function
        def my_method(self, arg1, arg2=None):
            return f"arg1={arg1}, arg2={arg2}"
    
    instance = MyClass()
    result = instance.my_method('value1', arg2='value2')
    assert result == "arg1=value1, arg2=value2"
    logger.debug.assert_called_with("{function}({args}, {kwargs})".format(function="my_method", args="arg1=value1", kwargs="arg2=value2"))
    logger.debug.assert_any("my_method -> arg1=value1, arg2=value2")

def test_logged_func_standalone_function():
    @logged_function
    def standalone_function(arg1, arg2=None):
        return f"arg1={arg1}, arg2={arg2}"
    
    result = standalone_function('value1', arg2='value2')
    assert result == "arg1=value1, arg2=value2"
    logger.debug.assert_called_with("{function}({args}, {kwargs})".format(function="standalone_function", args="arg1=value1", kwargs="arg2=value2"))
    logger.debug.assert_any("standalone_function -> arg1=value1, arg2=value2")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_semantic_release_helpers_logged_func_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_logged_func_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_logged_func_0.py:3: in <module>
    from semantic_release.helpers import logged_func
E   ImportError: cannot import name 'logged_func' from 'semantic_release.helpers' (/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_helpers_logged_func_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""