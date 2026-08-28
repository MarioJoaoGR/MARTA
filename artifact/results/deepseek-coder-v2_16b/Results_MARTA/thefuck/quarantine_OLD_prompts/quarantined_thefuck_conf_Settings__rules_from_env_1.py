
import pytest
from unittest.mock import patch, MagicMock
from thefuck.conf import Settings
import thefuck.const as const


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_valid_input_with_default_rules ______________________

    def test_valid_input_with_default_rules():
        settings = Settings()
        result = settings._rules_from_env('RULE1:RULE2:DEFAULT_RULES')
>       assert result == ['DEFAULT_RULES', 'RULE1', 'RULE2']
E       AssertionError: assert [<const: All ...LE1', 'RULE2'] == ['DEFAULT_RUL...LE1', 'RULE2']
E         
E         At index 0 diff: <const: All rules enabled> != 'DEFAULT_RULES'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_1.py:10: AssertionError
____________________ test_valid_input_without_default_rules ____________________

    def test_valid_input_without_default_rules():
        settings = Settings()
        result = settings._rules_from_env('RULE3:RULE4')
>       assert result == ['DEFAULT_RULES', 'RULE3', 'RULE4']
E       AssertionError: assert ['RULE3', 'RULE4'] == ['DEFAULT_RUL...LE3', 'RULE4']
E         
E         At index 0 diff: 'RULE3' != 'DEFAULT_RULES'
E         Right contains one more item: 'RULE4'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_1.py:15: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_1.py::test_valid_input_with_default_rules
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_1.py::test_valid_input_without_default_rules
========================= 2 failed, 1 warning in 0.17s =========================
"""