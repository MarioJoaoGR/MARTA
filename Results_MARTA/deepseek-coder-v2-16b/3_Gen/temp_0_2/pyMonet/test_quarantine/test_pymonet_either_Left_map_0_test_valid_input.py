
from pymonet.either import Left  # Assuming this is the correct module path

def test_valid_input():
    left_value = Left("valid_error")
    assert str(left_value) == "Left('valid_error')"

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

pyMonet/Test4DT_tests/test_pymonet_either_Left_map_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        left_value = Left("valid_error")
>       assert str(left_value) == "Left('valid_error')"
E       assert '<pymonet.eit...7f74473bf590>' == "Left('valid_error')"
E         
E         - Left('valid_error')
E         + <pymonet.either.Left object at 0x7f74473bf590>

pyMonet/Test4DT_tests/test_pymonet_either_Left_map_0_test_valid_input.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Left_map_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""