
import pytest
from thefuck.rules.git_add_force import match
from thefuck.command import Command

# Test 1: Match when command contains 'add' in script parts and output includes "Use -f if you really want to add them."
def test_match_when_valid():
    command_obj = Command(["git", "add"], "Use -f if you really want to add them.")
    assert match(command_obj) is True

# Test 2: Do not match when command contains 'add' in script parts but output does not include the specific message.
def test_match_when_invalid_output():
    command_obj = Command(["git", "add"], "Some other unrelated message.")
    assert match(command_obj) is False

# Test 3: Do not match when command does not contain 'add' in script parts but output includes the specific message.
def test_match_when_invalid_script():
    command_obj = Command(["git", "commit"], "Use -f if you really want to add them.")
    assert match(command_obj) is False

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
_________ ERROR collecting test_thefuck_rules_git_add_force_match_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_git_add_force_match_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_git_add_force_match_0.py:4: in <module>
    from thefuck.command import Command
E   ModuleNotFoundError: No module named 'thefuck.command'
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_git_add_force_match_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.20s ==========================
"""