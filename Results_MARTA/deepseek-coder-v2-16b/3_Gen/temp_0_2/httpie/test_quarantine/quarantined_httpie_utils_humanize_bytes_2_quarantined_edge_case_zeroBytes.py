
import pytest
from httpie.utils import humanize_bytes

def test_edge_case_zeroBytes():
    assert humanize_bytes(0) == '0 B'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_2_test_edge_case_zeroBytes.py F [100%]

=================================== FAILURES ===================================
___________________________ test_edge_case_zeroBytes ___________________________

    def test_edge_case_zeroBytes():
>       assert humanize_bytes(0) == '0 B'
E       AssertionError: assert '0.00 B' == '0 B'
E         
E         - 0 B
E         + 0.00 B

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_2_test_edge_case_zeroBytes.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_humanize_bytes_2_test_edge_case_zeroBytes.py::test_edge_case_zeroBytes
============================== 1 failed in 0.13s ===============================
"""