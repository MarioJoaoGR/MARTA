
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.network.sunos import SunOSNetwork

def test_invalid_input():
    with patch('ansible.module_utils.facts.network.sunos.SunOSNetwork') as mock_sunos:
        mock_instance = mock_sunos.return_value
        mock_instance.get_interfaces_info.side_effect = Exception("Invalid ifconfig output")

        with pytest.raises(Exception):
            SunOSNetwork().parse_ether_line(["ifconfig", "output", "for", "an", "interface"], {}, {"ipv4": [], "ipv6": []})
