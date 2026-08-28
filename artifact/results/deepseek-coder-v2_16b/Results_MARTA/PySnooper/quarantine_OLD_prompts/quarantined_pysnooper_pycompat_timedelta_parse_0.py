
import pytest
from datetime import timedelta as td
import pysnooper.pycompat as pycompat



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_pycompat_timedelta_parse_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_timedelta_parse_valid __________________________

    def test_timedelta_parse_valid():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_pycompat_timedelta_parse_0.py:7: Failed
__________________________ test_timedelta_parse_zero ___________________________

    def test_timedelta_parse_zero():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_pycompat_timedelta_parse_0.py:13: Failed
_________________________ test_timedelta_parse_invalid _________________________

    def test_timedelta_parse_invalid():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_pycompat_timedelta_parse_0.py:19: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_pycompat_timedelta_parse_0.py::test_timedelta_parse_valid
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_pycompat_timedelta_parse_0.py::test_timedelta_parse_zero
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_pycompat_timedelta_parse_0.py::test_timedelta_parse_invalid
============================== 3 failed in 0.27s ===============================
"""