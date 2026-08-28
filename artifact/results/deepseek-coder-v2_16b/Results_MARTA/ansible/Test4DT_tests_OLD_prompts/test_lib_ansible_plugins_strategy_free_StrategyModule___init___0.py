
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.strategy.free import StrategyModule


def test_strategy_module_base_throttling():
    with patch('ansible.plugins.strategy.free.StrategyModule.__init__', return_value=None):
        tqm_mock = MagicMock()
        strategy_module = StrategyModule(tqm_mock)
        assert not getattr(strategy_module, 'ALLOW_BASE_THROTTLING'), "The ALLOW_BASE_THROTTLING attribute should be False"