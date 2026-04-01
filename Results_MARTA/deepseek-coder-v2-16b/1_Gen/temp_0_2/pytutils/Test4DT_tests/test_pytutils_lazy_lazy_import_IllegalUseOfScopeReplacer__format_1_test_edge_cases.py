
import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_edge_cases():
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        raise IllegalUseOfScopeReplacer('test_name', 'This is a test error message')
    assert isinstance(exc_info.value, IllegalUseOfScopeReplacer), "Expected exception of type IllegalUseOfScopeReplacer"
