
from pymonet.either import Left, Right  # Import Left and Right from module 'pymonet.either'

def test_valid_input():
    left_error = Left("An error occurred")
    assert str(left_error) == 'Left("An error occurred")'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_either_Left_ap_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        left_error = Left("An error occurred")
>       assert str(left_error) == 'Left("An error occurred")'
E       assert '<pymonet.eit...7f51da46b150>' == 'Left("An error occurred")'
E         
E         - Left("An error occurred")
E         + <pymonet.either.Left object at 0x7f51da46b150>

pyMonet/Test4DT_tests/test_pymonet_either_Left_ap_0_test_valid_input.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Left_ap_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""