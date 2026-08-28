
import pytest
from ansible.utils.vars import combine_vars



def test_combine_vars_explicit_false():
    dict1 = {'a': 1, 'b': {'c': 2}}
    dict2 = {'b': {'d': 3}, 'e': 4}
    
    result = combine_vars(dict1, dict2, merge=False)
    assert result == {'a': 1, 'b': {'d': 3}, 'e': 4}