
import pytest
from pymonet.either import Left

def test_invalid_input():
    # Arrange
    non_callable = 'not_a_function'
    
    # Act and Assert
    with pytest.raises(TypeError):
        left_value = Left("error message")
        left_value.map(non_callable)

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

pyMonet/Test4DT_tests/test_pymonet_either_Left_map_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Arrange
        non_callable = 'not_a_function'
    
        # Act and Assert
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_either_Left_map_2_test_invalid_input.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Left_map_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""