
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.dnsclass import DnsFactCollector

# Test for valid input scenario
def test_valid_input():
    with patch('builtins.open', mock_open(read_data='nameserver 8.8.8.8\nnameserver 1.1.1.1\ndomain example.com\nsearch example.com localdomain\nsortlist 192.168.1.1\noptions timeout 5 attempts 2')):
        collector = DnsFactCollector()
        facts = collector.collect()
        assert 'dns' in facts
        assert 'nameservers' in facts['dns']
        assert facts['dns']['nameservers'] == ['8.8.8.8', '1.1.1.1']
        assert 'domain' in facts['dns']
        assert facts['dns']['domain'] == 'example.com'
        assert 'search' in facts['dns']
        assert facts['dns']['search'] == ['example.com', 'localdomain']
        assert 'sortlist' in facts['dns']
        assert facts['dns']['sortlist'] == ['192.168.1.1']
        assert 'options' in facts['dns']
        assert facts['dns']['options'] == {'timeout': 5, 'attempts': 2}

# Test for missing file scenario
def test_missing_file():
    with patch('builtins.open', side_effect=FileNotFoundError):
        collector = DnsFactCollector()
        with pytest.raises(Exception) as e:
            collector.collect()
        assert str(e.value) == "Could not read /etc/resolv.conf"

# Test for invalid content scenario
def test_invalid_content():
    with patch('builtins.open', mock_open(read_data='invalid content')):
        collector = DnsFactCollector()
        facts = collector.collect()
        assert 'dns' in facts
        assert not hasattr(facts['dns'], 'nameservers')
        assert not hasattr(facts['dns'], 'domain')
        assert not hasattr(facts['dns'], 'search')
        assert not hasattr(facts['dns'], 'sortlist')
        assert not hasattr(facts['dns'], 'options')
