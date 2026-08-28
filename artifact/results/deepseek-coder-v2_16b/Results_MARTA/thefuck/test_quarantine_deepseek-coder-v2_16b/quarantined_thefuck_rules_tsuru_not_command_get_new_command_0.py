
import pytest
from thefuck.types import Command
from thefuck.rules.tsuru_not_command import get_new_command



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_tsuru_not_command_get_new_command_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        cmd_obj = Command("some script", "tsuru: \"git status\" is not a tsuru command")
        result = get_new_command(cmd_obj)
>       assert result == ['git add', 'git commit']
E       AssertionError: assert [] == ['git add', 'git commit']
E         
E         Right contains 2 more items, first extra item: 'git add'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_tsuru_not_command_get_new_command_0.py:9: AssertionError
______________________________ test_missing_lines ______________________________

    def test_missing_lines():
        cmd_obj = Command("some script", "tsuru: \"git status\" is not a tsuru command")
>       with pytest.raises(IndexError):
E       Failed: DID NOT RAISE <class 'IndexError'>

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_tsuru_not_command_get_new_command_0.py:13: Failed
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        cmd_obj = Command("some script", None)
>       result = get_new_command(cmd_obj)

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_tsuru_not_command_get_new_command_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/rules/tsuru_not_command.py:12: in get_new_command
    broken_cmd = re.findall(r'tsuru: "([^"]*)" is not a tsuru command',
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

pattern = 'tsuru: "([^"]*)" is not a tsuru command', string = None, flags = 0

    def findall(pattern, string, flags=0):
        """Return a list of all non-overlapping matches in the string.
    
        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.
    
        Empty matches are included in the result."""
>       return _compile(pattern, flags).findall(string)
E       TypeError: expected string or bytes-like object

/opt/conda/envs/test4py_env/lib/python3.10/re.py:240: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_tsuru_not_command_get_new_command_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_tsuru_not_command_get_new_command_0.py::test_missing_lines
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_tsuru_not_command_get_new_command_0.py::test_invalid_input
========================= 3 failed, 1 warning in 0.18s =========================
"""