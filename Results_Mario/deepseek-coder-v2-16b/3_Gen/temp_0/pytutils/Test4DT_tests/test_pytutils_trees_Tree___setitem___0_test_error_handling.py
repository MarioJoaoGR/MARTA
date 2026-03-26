
import pytest
from pytutils.trees import Tree

def test_error_handling():
    t = Tree({'a': 1, 'b': {'c': 2}})
    
    # Attempt to set a value with an empty namespace key
    with pytest.raises(ValueError):
        t['key'] = 'value'
