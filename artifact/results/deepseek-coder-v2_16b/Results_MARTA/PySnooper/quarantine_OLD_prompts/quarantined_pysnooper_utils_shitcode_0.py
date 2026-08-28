
import pytest
from pysnooper.utils import shitcode

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_shitcode_0.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_non_ascii ___________________________

    def test_valid_case_non_ascii():
>       assert shitcode("こんにちは世界") == "??????????????"
E       AssertionError: assert '???????' == '??????????????'
E         
E         - ??????????????
E         + ???????

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_shitcode_0.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_shitcode_0.py::test_valid_case_non_ascii
============================== 1 failed in 0.08s ===============================
"""