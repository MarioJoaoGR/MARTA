
import pytest
from thefuck.conf import Settings




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_rules_from_env_with_default _______________________

    def test_rules_from_env_with_default():
        settings = Settings()
        result = settings._rules_from_env('RULE1:RULE2:DEFAULT_RULES')
>       assert result == ['DEFAULT_RULES', 'RULE1', 'RULE2']
E       AssertionError: assert [<const: All ...LE1', 'RULE2'] == ['DEFAULT_RUL...LE1', 'RULE2']
E         
E         At index 0 diff: <const: All rules enabled> != 'DEFAULT_RULES'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py:8: AssertionError
_____________________ test_rules_from_env_without_default ______________________

    def test_rules_from_env_without_default():
        settings = Settings()
        result = settings._rules_from_env('RULE3:RULE4')
>       assert result == ['DEFAULT_RULES', 'RULE3', 'RULE4']
E       AssertionError: assert ['RULE3', 'RULE4'] == ['DEFAULT_RUL...LE3', 'RULE4']
E         
E         At index 0 diff: 'RULE3' != 'DEFAULT_RULES'
E         Right contains one more item: 'RULE4'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py:13: AssertionError
__________________________ test_rules_from_env_empty ___________________________

    def test_rules_from_env_empty():
        settings = Settings()
        result = settings._rules_from_env('')
>       assert result == ['DEFAULT_RULES']
E       AssertionError: assert [''] == ['DEFAULT_RULES']
E         
E         At index 0 diff: '' != 'DEFAULT_RULES'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py:18: AssertionError
_______________________ test_rules_from_env_only_default _______________________

    def test_rules_from_env_only_default():
        settings = Settings()
        result = settings._rules_from_env('DEFAULT_RULES')
>       assert result == ['DEFAULT_RULES']
E       AssertionError: assert [<const: All rules enabled>] == ['DEFAULT_RULES']
E         
E         At index 0 diff: <const: All rules enabled> != 'DEFAULT_RULES'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py:23: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py::test_rules_from_env_with_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py::test_rules_from_env_without_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py::test_rules_from_env_empty
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings__rules_from_env_0.py::test_rules_from_env_only_default
========================= 4 failed, 1 warning in 0.13s =========================
"""