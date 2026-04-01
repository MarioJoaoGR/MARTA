
import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_invalid_inputs():
    with pytest.raises(IllegalUseOfScopeReplacer) as exc_info:
        raise IllegalUseOfScopeReplacer('example', 'This is an example of misuse.')
    assert isinstance(exc_info.value, IllegalUseOfScopeReplacer), "Expected exception type mismatch"
