
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.strategy import host_pinned

def test_init_with_valid_tqm():
    class MockTQM:
        pass
    
    mock_tqm = MockTQM()
    with patch('ansible.plugins.strategy.host_pinned.StrategyModule', lambda x: MagicMock(tqm=x, _host_pinned=True)):
        strategy_module = host_pinned.StrategyModule(mock_tqm)
        assert hasattr(strategy_module, '_host_pinned')
        assert strategy_module._host_pinned is True
