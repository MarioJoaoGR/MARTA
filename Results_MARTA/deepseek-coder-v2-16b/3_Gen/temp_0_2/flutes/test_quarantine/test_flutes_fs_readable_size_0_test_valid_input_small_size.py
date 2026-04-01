
from flutes.fs import readable_size

def test_valid_input_small_size():
    assert readable_size(500) == "500.00B"

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

flutes/Test4DT_tests/test_flutes_fs_readable_size_0_test_valid_input_small_size.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_small_size __________________________

    def test_valid_input_small_size():
>       assert readable_size(500) == "500.00B"
E       AssertionError: assert '500.00' == '500.00B'
E         
E         - 500.00B
E         ?       -
E         + 500.00

flutes/Test4DT_tests/test_flutes_fs_readable_size_0_test_valid_input_small_size.py:5: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_readable_size_0_test_valid_input_small_size.py::test_valid_input_small_size
============================== 1 failed in 0.08s ===============================
"""