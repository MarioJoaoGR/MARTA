
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.vars import combine_vars, C

# Scenario 1: Test standard merge behavior with two dictionaries
def test_valid_merge_behavior():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'b': {'d': 3}, 'e': 4}
    
    with patch.object(C, 'DEFAULT_HASH_BEHAVIOUR', 'merge'):
        result = combine_vars(dict1, dict2)
        assert result == {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}

# Scenario 2: Test replace behavior with two dictionaries where merge is set to False
def test_replace_behavior():
    dict1 = {'a': [1, 2], 'b': {'c': 2}}
    dict2 = {'b': {'d': 3}, 'e': [6]}
    
    result = combine_vars(dict1, dict2, merge=False)
    assert result == {'a': [1, 2], 'b': {'d': 3}, 'e': [6]}

# Scenario 3: Test default behavior where the function decides whether to merge or replace based on C.DEFAULT_HASH_BEHAVIOUR
def test_default_behavior():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'b': {'d': 3}, 'e': 4}
    
    with patch.object(C, 'DEFAULT_HASH_BEHAVIOUR', 'merge'):
        result = combine_vars(dict1, dict2)
        assert result == {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    
    with patch.object(C, 'DEFAULT_HASH_BEHAVIOUR', 'replace'):
        result = combine_vars(dict1, dict2)
        assert result == {'a': 1, 'b': {'d': 3}, 'e': 4}
