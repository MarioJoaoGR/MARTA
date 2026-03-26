
from unittest.mock import MagicMock
import pytest
from pymonet.semigroups import Map  # Assuming the correct module path is known

def test_concat():
    # Create mock Semigroup instances
    sem1 = MagicMock()
    sem2 = MagicMock()
    sem3 = MagicMock()
    sem4 = MagicMock()
    
    # Create a map with initial values
    m1 = Map({'a': sem1, 'b': sem2})
    m2 = Map({'a': sem3, 'b': sem4})
    
    # Mock the concat method of Semigroup instances
    sem1.concat.return_value = MagicMock()
    sem2.concat.return_value = MagicMock()
    sem3.concat.return_value = MagicMock()
    sem4.concat.return_value = MagicMock()
    
    # Perform the concatenation
    concatenated_map = m1.concat(m2)
    
    # Assert that the concat method was called correctly
    assert isinstance(concatenated_map, Map)
    assert len(concatenated_map.value) == 2
    assert concatenated_map.value['a'] == sem1.concat.return_value
    assert concatenated_map.value['b'] == sem2.concat.return_value
