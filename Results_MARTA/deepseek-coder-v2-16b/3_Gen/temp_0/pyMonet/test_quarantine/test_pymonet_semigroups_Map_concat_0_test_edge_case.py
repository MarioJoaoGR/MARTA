
from pymonet.semigroups import Semigroup  # Assuming this is the correct module path
from collections import defaultdict

class Map(Semigroup):
    """
    A Map is a Semigroup that stores key-value pairs where the value part of each pair is itself a semigroup and supports concatenation. The `concat` method concatenates all values in the map by applying the concatenation operation on corresponding values from two maps.
    
    Parameters:
        value (dict): A dictionary where keys are arbitrary and values are instances of Semigroup. This dictionary represents the initial state of the Map.
        
    Attributes:
        value (dict): The dictionary containing key-value pairs, where each value is an instance of Semigroup.
    
    Methods:
        concat(self, semigroup): Concatenates this map with another map by applying concatenation to corresponding values.
            Parameters:
                semigroup (Map[B]): Another Map instance whose values are to be concatenated with the current map's values.
            Returns:
                new Map with concated all values: A new Map instance where each value is the result of concatenating the corresponding values from this map and the provided semigroup map.
    
    Examples:
        >>> m1 = Map({'a': Semigroup(1), 'b': Semigroup(2)})
        >>> m2 = Map({'a': Semigroup(3), 'b': Semigroup(4)})
        >>> concatenated_map = m1.concat(m2)
        >>> print(concatenated_map.value)  # Output will be {'a': Semigroup(1+3), 'b': Semigroup(2+4)}
    
    Note:
        The Map class assumes that the values in the dictionary are instances of Semigroup and supports concatenation as defined by the Semigroup's `concat` method.
    """
    def concat(self, semigroup):
        """
        :param semigroup: other semigroup to concat
        :type semigroup: Map[B]
        :returns: new Map with concated all values
        :rtype: Map[A]
        """
        # Create a defaultdict to store the concatenated results
        concatenated_value = defaultdict(Semigroup)
        
        # Concatenate corresponding Semigroup instances
        for key, value in self.value.items():
            if key in semigroup.value:
                concatenated_value[key] = value.concat(semigroup.value[key])
            else:
                concatenated_value[key] = value  # If the key is not present in the other map, just take the current value
        
        return Map({k: v for k, v in concatenated_value.items()})

# Test case to verify the concatenation functionality
def test_edge_case():
    class MockSemigroup:
        def __init__(self, val):
            self.val = val
    
        def concat(self, other):
            return MockSemigroup(self.val + other.val)
    
    m1 = Map({'a': MockSemigroup(1), 'b': MockSemigroup(2)})
    m2 = Map({'a': MockSemigroup(3), 'b': MockSemigroup(4)})
    
    concatenated_map = m1.concat(m2)
    
    assert concatenated_map.value == {'a': MockSemigroup(4), 'b': MockSemigroup(6)}

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        class MockSemigroup:
            def __init__(self, val):
                self.val = val
    
            def concat(self, other):
                return MockSemigroup(self.val + other.val)
    
        m1 = Map({'a': MockSemigroup(1), 'b': MockSemigroup(2)})
        m2 = Map({'a': MockSemigroup(3), 'b': MockSemigroup(4)})
    
        concatenated_map = m1.concat(m2)
    
>       assert concatenated_map.value == {'a': MockSemigroup(4), 'b': MockSemigroup(6)}
E       AssertionError: assert {'a': <Test4D...7faa1255ad90>} == {'a': <Test4D...7faa1255ab50>}
E         
E         Differing items:
E         {'a': <Test4DT_tests.test_pymonet_semigroups_Map_concat_0_test_edge_case.test_edge_case.<locals>.MockSemigroup object at 0x7faa1255a850>} != {'a': <Test4DT_tests.test_pymonet_semigroups_Map_concat_0_test_edge_case.test_edge_case.<locals>.MockSemigroup object at 0x7faa1255acd0>}
E         {'b': <Test4DT_tests.test_pymonet_semigroups_Map_concat_0_test_edge_case.test_edge_case.<locals>.MockSemigroup object at 0x7faa1255ad90>} != {'b': <Test4DT_tests.test_pymonet_semigroups_Map_concat_0_test_edge_case.test_edge_case.<locals>.MockSemigroup object at 0x7faa1255ab50>}
E         Use -v to get more diff

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_case.py:64: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""