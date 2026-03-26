
from pymonet.semigroups import Semigroup  # Assuming the correct module path is used
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
        return Map(
            {key: value.concat(semigroup.value[key]) for key, value in self.value.items()}
        )

# MockSemigroup class definition
class MockSemigroup:
    def __init__(self, val):
        self.val = val
    
    def concat(self, other):
        return MockSemigroup(self.val + other.val)
    
    # Override the equality method to compare values instead of memory addresses
    def __eq__(self, other):
        if isinstance(other, MockSemigroup):
            return self.val == other.val
        return False

# Test case definition
def test_edge_case():
    # Create two Map instances with MockSemigroup values
    m1 = Map({'a': MockSemigroup(1), 'b': MockSemigroup(2)})
    m2 = Map({'a': MockSemigroup(3), 'b': MockSemigroup(4)})
    
    # Concatenate the maps
    concatenated_map = m1.concat(m2)
    
    # Assert that the concatenation result is as expected
    assert concatenated_map.value == {'a': MockSemigroup(4), 'b': MockSemigroup(6)}
