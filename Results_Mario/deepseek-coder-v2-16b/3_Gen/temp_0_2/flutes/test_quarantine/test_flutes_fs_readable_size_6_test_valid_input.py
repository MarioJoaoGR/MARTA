
import pytest
from flutes.fs import readable_size

def test_valid_input():
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(500000) == "488.28K"
    assert readable_size(123456789) == "117.74M"
    assert readable_size(1000) == "1000.00B"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        assert readable_size(1024 * 1024) == "1.00M"
        assert readable_size(500000) == "488.28K"
        assert readable_size(123456789) == "117.74M"
>       assert readable_size(1000) == "1000.00B"
E       AssertionError: assert '1000.00' == '1000.00B'
E         
E         - 1000.00B
E         ?        -
E         + 1000.00

flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_6_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""