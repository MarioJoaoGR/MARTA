
import pytest
from ansible.plugins.lookup import sequence

@pytest.fixture(scope="module")
def lookup_module():
    lm = sequence.LookupModule()
    lm.reset()
    return lm

# Test Scenario 1: test_valid_inputs
def test_valid_inputs(lookup_module):
    result = lookup_module.generate_sequence(terms=[])
    assert result == ["1"]
    
    result = lookup_module.generate_sequence(terms=[], start=5, end=10)
    assert result == ["5", "6", "7", "8", "9", "10"]
    
    result = lookup_module.generate_sequence(terms=[], start=2, end=8, stride=2, format="0x%02x")
    assert result == ["0x02", "0x04", "0x06", "0x08"]
    
    result = lookup_module.generate_sequence(terms=[], count=5)
    assert result == ["1", "2", "3", "4", "5"]
    
    result = lookup_module.generate_sequence(terms=[], start=0x0f00, count=4, stride=1, format="%04x")
    assert result == ["0f00", "0f01", "0f02", "0f03"]
    
    result = lookup_module.generate_sequence(terms=[], start=1, count=5)
    assert result == ["1", "2", "3", "4", "5"]

# Test Scenario 2: test_edge_cases
def test_edge_cases(lookup_module):
    with pytest.raises(Exception):
        lookup_module.generate_sequence(terms=[], start=None, end=None)
    
    result = lookup_module.generate_sequence(terms=[], start=5, end=5)
    assert result == ["5"]
    
    with pytest.raises(Exception):
        lookup_module.generate_sequence(terms=[], count=0)
    
    with pytest.raises(Exception):
        lookup_module.generate_sequence(terms=[], start=-1, end=5)

# Test Scenario 3: test_invalid_inputs
def test_invalid_inputs():
    lm = sequence.LookupModule()
    with pytest.raises(TypeError):
        lm.generate_sequence(terms=[], invalid_param="test")
