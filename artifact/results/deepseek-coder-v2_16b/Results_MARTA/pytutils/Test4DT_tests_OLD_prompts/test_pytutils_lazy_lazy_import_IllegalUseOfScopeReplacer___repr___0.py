
import pytest
from pytutils.lazy.lazy_import import lazy_import

# Define the test scenarios
def test_basic_usage():
    with pytest.raises(ModuleNotFoundError):
        from IllegalUseOfScopeReplacer import IllegalUseOfScopeReplacer

def test_with_extra_info():
    with pytest.raises(ModuleNotFoundError):
        from IllegalUseOfScopeReplacer import IllegalUseOfScopeReplacer
