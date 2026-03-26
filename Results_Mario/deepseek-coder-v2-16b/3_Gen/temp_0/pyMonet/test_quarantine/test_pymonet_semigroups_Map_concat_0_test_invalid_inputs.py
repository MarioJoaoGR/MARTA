
import pytest
from pymonet.semigroups import Semigroup, Map  # Import Semigroup and Map from the correct module

def test_invalid_inputs():
    # Create a mock Semigroup instance
    semigroup1 = Semigroup(1)
    semigroup2 = Semigroup(2)

    # Create a map with valid Semigroup instances
    map1 = Map({'a': semigroup1, 'b': semigroup2})

    # Try to create another map with invalid input (not Semigroup instance)
    with pytest.raises(TypeError):
        Map({'a': 1, 'b': 2})  # This should raise TypeError because 1 and 2 are not Semigroup instances

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Create a mock Semigroup instance
        semigroup1 = Semigroup(1)
        semigroup2 = Semigroup(2)
    
        # Create a map with valid Semigroup instances
        map1 = Map({'a': semigroup1, 'b': semigroup2})
    
        # Try to create another map with invalid input (not Semigroup instance)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================
"""