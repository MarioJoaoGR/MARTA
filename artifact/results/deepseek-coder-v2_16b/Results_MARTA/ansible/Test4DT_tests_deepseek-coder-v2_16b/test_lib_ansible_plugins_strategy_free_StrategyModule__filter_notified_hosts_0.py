
import pytest
from ansible.plugins.strategy import free



def test_invalid_input():
    with pytest.raises(AttributeError):
        strategy = free.StrategyModule(None)  # Passing None instead of a valid tqm object