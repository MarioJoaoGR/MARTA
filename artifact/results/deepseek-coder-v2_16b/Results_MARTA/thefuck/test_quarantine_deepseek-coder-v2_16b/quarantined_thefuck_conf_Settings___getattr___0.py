
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings___getattr___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        settings = Settings()
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings___getattr___0.py:7: Failed
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        settings = Settings()
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings___getattr___0.py:12: Failed
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings___getattr___0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_conf_Settings___getattr___0.py::test_error_handling
========================= 2 failed, 1 warning in 0.12s =========================
"""