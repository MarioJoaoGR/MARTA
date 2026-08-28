
import pytest
from your_module import combine_vars  # Replace 'your_module' with the actual module name where `combine_vars` is defined

# Scenario 1: Test valid inputs
def test_valid_inputs():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'b': {'d': 3}, 'e': 4}
    dict3 = {'a': [1, 2], 'b': {'c': 2}}
    dict4 = {'b': {'c': 3, 'd': [4, 5]}, 'e': [6]}
    
    # Test default merge behavior
    result1 = combine_vars(dict1, dict2)
    assert result1 == {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    
    # Test replace behavior with explicit True
    result2 = combine_vars(dict3, dict4, merge=True)
    assert result2 == {'a': [1, 2], 'b': {'c': 3, 'd': [4, 5]}, 'e': [6]}
    
    # Test replace behavior with explicit False
    result3 = combine_vars(dict3, dict4, merge=False)
    assert result3 == {'a': [1, 2], 'b': {'c': 3, 'd': [4, 5]}, 'e': [6]}
    
    # Test replace behavior with None (default behavior)
    result4 = combine_vars(dict3, dict4)
    assert result4 == {'a': [1, 2], 'b': {'c': 3, 'd': [4, 5]}, 'e': [6]}

# Scenario 2: Test edge cases with None and empty values
def test_edge_cases():
    dict1 = {}
    dict2 = None
    dict3 = {'a': [], 'b': {}}
    
    # Test with None
    result1 = combine_vars(dict1, dict2)
    assert result1 == {}
    
    # Test with empty dictionaries
    result2 = combine_vars(dict1, dict3)
    assert result2 == {'a': [], 'b': {}}
    
    # Test with merge set to False
    result3 = combine_vars(dict3, dict1, merge=False)
    assert result3 == {'a': [], 'b': {}}

# Scenario 3: Test invalid inputs with non-dictionary types and error handling
def test_invalid_inputs():
    dict1 = 1
    dict2 = 'string'
    
    # Test with non-dictionary type
    with pytest.raises(TypeError):
        combine_vars(dict1, dict2)
    
    # Test with merge set to True (should raise TypeError as well)
    with pytest.raises(TypeError):
        combine_vars(dict1, dict2, merge=True)
