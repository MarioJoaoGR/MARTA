
import pytest
from ansible.vars.manager import VarsWithSources

def test_valid_inputs():
    vs = VarsWithSources({'var1': 1, 'var2': 2})
    vs.sources['var1'] = 'file_name:line_number'
    assert vs['var1'] == 1

def test_edge_cases():
    vs = VarsWithSources()
    with pytest.raises(KeyError):
        vs['nonexistent_key']

def test_invalid_inputs():
    with pytest.raises(TypeError):
        vs = VarsWithSources(12345)  # Passing an integer instead of a dictionary
    
    vs = VarsWithSources({'var1': 1})
    with pytest.raises(KeyError):
        del vs['nonexistent_key']  # Attempting to delete a non-existent key
