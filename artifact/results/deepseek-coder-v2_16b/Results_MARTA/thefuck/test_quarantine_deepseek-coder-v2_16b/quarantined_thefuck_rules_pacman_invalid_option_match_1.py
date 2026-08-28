
import pytest
from thefuck.types import Command
from thefuck.rules.pacman_invalid_option import match



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_pacman_invalid_option_match_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_match_with_invalid_option ________________________

    def test_match_with_invalid_option():
        command = Command("echo 'Hello, World!' -x", "error: invalid option '-x'")
>       assert match(command)
E       AssertionError: assert False
E        +  where False = match(Command(script=echo 'Hello, World!' -x, output=error: invalid option '-x'))

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_pacman_invalid_option_match_1.py:8: AssertionError
___________________ test_match_with_different_invalid_option ___________________

    def test_match_with_different_invalid_option():
        command = Command("echo 'Hello, World!' -r", "error: invalid option '-r'")
>       assert match(command)
E       AssertionError: assert False
E        +  where False = match(Command(script=echo 'Hello, World!' -r, output=error: invalid option '-r'))

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_pacman_invalid_option_match_1.py:12: AssertionError
___________________ test_match_with_multiple_invalid_options ___________________

    def test_match_with_multiple_invalid_options():
        command = Command("echo 'Hello, World!' -x -r", "error: invalid option '-r'")
>       assert match(command)
E       AssertionError: assert False
E        +  where False = match(Command(script=echo 'Hello, World!' -x -r, output=error: invalid option '-r'))

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_pacman_invalid_option_match_1.py:16: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/types.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_pacman_invalid_option_match_1.py::test_match_with_invalid_option
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_pacman_invalid_option_match_1.py::test_match_with_different_invalid_option
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_pacman_invalid_option_match_1.py::test_match_with_multiple_invalid_options
========================= 3 failed, 1 warning in 0.18s =========================
"""