
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.plugins.strategy.linear import StrategyModule



def test_invalid_input():
    with pytest.raises(TypeError):
        strategy_module = StrategyModule()