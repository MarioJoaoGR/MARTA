
import pytest
import re
from pytutils.lazy import lazy_regex

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_regex_reset_compile_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_no_re_module _______________________________

    def test_no_re_module():
        """Test that ImportError is raised when trying to access re.compile without patching."""
>       with pytest.raises(ImportError):
E       Failed: DID NOT RAISE <class 'ImportError'>

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_regex_reset_compile_1.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_regex_reset_compile_1.py::test_no_re_module
============================== 1 failed in 0.04s ===============================
"""