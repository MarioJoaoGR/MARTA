
import pytest
from httpie.utils import humanize_bytes


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________ test_humanize_bytes_default_precision _____________________

    def test_humanize_bytes_default_precision():
        assert humanize_bytes(1) == '1 B'
>       assert humanize_bytes(1024) == '1.0 kB'
E       AssertionError: assert '1.00 kB' == '1.0 kB'
E         
E         - 1.0 kB
E         + 1.00 kB
E         ?    +

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_0.py:7: AssertionError
_____________________ test_humanize_bytes_custom_precision _____________________

    def test_humanize_bytes_custom_precision():
>       assert humanize_bytes(1, precision=1) == '1.0 B'
E       AssertionError: assert '1 B' == '1.0 B'
E         
E         - 1.0 B
E         ?  --
E         + 1 B

/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_0.py::test_humanize_bytes_default_precision
FAILED ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_0.py::test_humanize_bytes_custom_precision
============================== 2 failed in 0.17s ===============================
"""