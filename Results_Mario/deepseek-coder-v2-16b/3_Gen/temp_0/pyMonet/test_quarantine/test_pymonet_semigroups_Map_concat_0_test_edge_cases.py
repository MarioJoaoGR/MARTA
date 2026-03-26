
from pymonet.semigroups import Semigroup
import pytest

def test_concat():
    # Create two Map instances with Semigroup values
    m1 = Map({'a': Semigroup(1), 'b': Semigroup(2)})
    m2 = Map({'a': Semigroup(3), 'b': Semigroup(4)})
    
    # Concatenate the maps
    concatenated_map = m1.concat(m2)
    
    # Check that the concatenation was performed correctly
    assert concatenated_map.value == {'a': Semigroup(1 + 3), 'b': Semigroup(2 + 4)}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Map_concat_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_cases.py:7:9: E0602: Undefined variable 'Map' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_cases.py:8:9: E0602: Undefined variable 'Map' (undefined-variable)


"""