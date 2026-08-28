
import pytest
from apimd.loader import _write
from os.path import isfile

# Test for invalid path, which should raise FileNotFoundError
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_path _______________________________

    def test_invalid_path():
>       with pytest.raises(FileNotFoundError):
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_loader__write_0.py::test_invalid_path
============================== 1 failed in 0.06s ===============================
"""