
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.other.facter import FacterFactCollector

def test_collect_with_valid_output():
    with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.get_facter_output', return_value='{"key": "value"}') as mock_get_facter_output:
        fact_collector = FacterFactCollector()
        result = fact_collector.collect(module=MagicMock())
        assert isinstance(result, dict)
        assert len(result) == 1
        mock_get_facter_output.assert_called_once()

def test_collect_with_invalid_json():
    with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.get_facter_output', return_value='invalid json') as mock_get_facter_output:
        fact_collector = FacterFactCollector()
        result = fact_collector.collect(module=MagicMock())
        assert isinstance(result, dict)
        assert len(result) == 0
        mock_get_facter_output.assert_called_once()

def test_collect_without_output():
    with patch('ansible.module_utils.facts.other.facter.FacterFactCollector.get_facter_output', return_value=None) as mock_get_facter_output:
        fact_collector = FacterFactCollector()
        result = fact_collector.collect(module=MagicMock())
        assert isinstance(result, dict)
        assert len(result) == 0
        mock_get_facter_output.assert_called_once()
