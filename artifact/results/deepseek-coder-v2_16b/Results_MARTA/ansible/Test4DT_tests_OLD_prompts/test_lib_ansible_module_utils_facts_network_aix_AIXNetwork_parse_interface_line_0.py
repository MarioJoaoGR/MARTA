
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.network.aix import AIXNetwork

def test_valid_input():
    with patch('ansible.module_utils.facts.network.aix.AIXNetwork.__init__', return_value=None):
        aix_network = AIXNetwork()
        words = ['eth0:', 'UP,BROADCAST,RUNNING,MULTICAST']
        result = aix_network.parse_interface_line(words)
        assert isinstance(result, dict), "Expected a dictionary but got something else"
        assert 'device' in result, "Expected 'device' key to be present in the dictionary"
        assert result['device'] == 'eth0', f"Expected 'device' to be 'eth0' but got {result['device']}"

def test_missing_lines():
    with patch('ansible.module_utils.facts.network.aix.AIXNetwork.__init__', return_value=None):
        aix_network = AIXNetwork()
        words = ['eth0:', 'UP,BROADCAST,RUNNING,MULTICAST']
        result = aix_network.parse_interface_line(words)
        assert isinstance(result, dict), "Expected a dictionary but got something else"
        assert 'device' in result, "Expected 'device' key to be present in the dictionary"
        assert result['device'] == 'eth0', f"Expected 'device' to be 'eth0' but got {result['device']}"

def test_invalid_input():
    with patch('ansible.module_utils.facts.network.aix.AIXNetwork.__init__', return_value=None):
        aix_network = AIXNetwork()
        words = ['eth0:', 'UP,BROADCAST,RUNNING,MULTICAST']
        result = aix_network.parse_interface_line(words)
        assert isinstance(result, dict), "Expected a dictionary but got something else"
        assert 'device' in result, "Expected 'device' key to be present in the dictionary"
        assert result['device'] == 'eth0', f"Expected 'device' to be 'eth0' but got {result['device']}"
