
import pytest
from pymonet.either import Right

def test_invalid_input():
    right_instance = Right(42)

    # Test with a valid mapper function
    def double(x):
        return x * 2

    mapped_value = right_instance.bind(double)
    assert mapped_value == 84

    # Test with an invalid mapper function (should raise an error or return the original value)
    def invalid_mapper(x):
        if isinstance(x, int):
            return x * 2
        else:
            raise ValueError("Invalid input")

    with pytest.raises(ValueError):
        right_instance.bind(invalid_mapper)

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

pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        right_instance = Right(42)
    
        # Test with a valid mapper function
        def double(x):
            return x * 2
    
        mapped_value = right_instance.bind(double)
        assert mapped_value == 84
    
        # Test with an invalid mapper function (should raise an error or return the original value)
        def invalid_mapper(x):
            if isinstance(x, int):
                return x * 2
            else:
                raise ValueError("Invalid input")
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_2_test_invalid_input.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Right_bind_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""