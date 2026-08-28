
import pytest
from pymonet.monad_try import Try

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_monad_try_Try_on_success_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_on_success ________________________________

    def test_on_success():
        def success_callback(val):
            assert val == "success"
    
        try1 = Try("success", True)
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_monad_try_Try_on_success_0.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_monad_try_Try_on_success_0.py::test_on_success
============================== 1 failed in 0.05s ===============================
"""