
from pymonet.either import Right
import pytest

def test_invalid_input():
    right_string = Right('string')

    def mapper(x):
        return int(x)  # Correctly convert string to integer

    with pytest.raises(TypeError):
        right_string.map(mapper)

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

pyMonet/Test4DT_tests/test_pymonet_either_Right_map_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        right_string = Right('string')
    
        def mapper(x):
            return int(x)  # Correctly convert string to integer
    
        with pytest.raises(TypeError):
>           right_string.map(mapper)

pyMonet/Test4DT_tests/test_pymonet_either_Right_map_2_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/either.py:162: in map
    return Right(mapper(self.value))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 'string'

    def mapper(x):
>       return int(x)  # Correctly convert string to integer
E       ValueError: invalid literal for int() with base 10: 'string'

pyMonet/Test4DT_tests/test_pymonet_either_Right_map_2_test_invalid_input.py:9: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Right_map_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""