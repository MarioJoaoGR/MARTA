
import pytest
from ansible.module_utils.facts.system.dns import DnsFactCollector

# Test case for collecting DNS facts from /etc/resolv.conf with no content
def test_collect_empty_dns_file():
    collector = DnsFactCollector()
    dns_facts = collector.collect()
    
    assert isinstance(dns_facts, dict), "The result should be a dictionary"