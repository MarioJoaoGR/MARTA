
import pytest
from unittest.mock import patch
from thonny.jedi_utils import ThonnyCompletion, _tweak_completions

# Test scenarios
def test_valid_case():
    completions = [
        ThonnyCompletion(name='foo', complete='bar=', type='type1', description='desc1', parent='parent1', full_name='full1'),
        ThonnyCompletion(name='baz', complete='qux=', type='type2', description='desc2', parent='parent2', full_name='full2')
    ]
    
    tweaked_completions = _tweak_completions(completions)
    
    assert all(comp.name.endswith('=') for comp in tweaked_completions)
    assert len(tweaked_completions) == 2

def test_edge_case():
    completions = []
    
    tweaked_completions = _tweak_completions(completions)
    
    assert not tweaked_completions

def test_invalid_input():
    with pytest.raises(TypeError):
        _tweak_completions(None)
