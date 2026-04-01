
import pytest
from unittest.mock import MagicMock
from pymonet.semigroups import Map  # Assuming this is the correct module path

def test_valid_inputs():
    # Create mock Semigroup instances
    sem1 = MagicMock()
    sem2 = MagicMock()
    sem3 = MagicMock()
    sem4 = MagicMock()
    
    # Create a mock Map instance with initial values
    m1 = Map({'a': sem1, 'b': sem2})
    m2 = Map({'a': sem3, 'b': sem4})
    
    # Mock the concat method of Semigroup instances
    sem1.concat.return_value = MagicMock()
    sem2.concat.return_value = MagicMock()
    sem3.concat.return_value = MagicMock()
    sem4.concat.return_value = MagicMock()
    
    # Call the concat method of Map instance
    concatenated_map = m1.concat(m2)
    
    # Assert that the resulting map has the correct values after concatenation
    assert isinstance(concatenated_map, Map)
    assert len(concatenated_map.value) == 2
    assert concatenated_map.value['a'] == sem1.concat.return_value
    assert concatenated_map.value['b'] == sem2.concat.return_value
    
    # Optionally, you can add more assertions to check the exact values or behavior
