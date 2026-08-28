
import pytest
from unittest.mock import patch
import re
from pytutils.lazy.lazy_regex import lazy_compile, reset_compile

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_regex_install_lazy_compile_0.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        with pytest.raises(ValueError):
            class InvalidCompile:
                pass
            with patch('re.compile', new=InvalidCompile()):
>               re.compile('pattern')
E               TypeError: 'InvalidCompile' object is not callable

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_regex_install_lazy_compile_0.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_lazy_lazy_regex_install_lazy_compile_0.py::test_error_handling
============================== 1 failed in 0.04s ===============================
"""