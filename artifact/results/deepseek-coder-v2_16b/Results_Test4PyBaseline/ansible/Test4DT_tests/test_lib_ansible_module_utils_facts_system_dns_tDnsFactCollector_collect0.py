# Module: ansible.module_utils.facts.system.dns
import pytest
from ansible.module_utils.facts.system.dns import DnsFactCollector

# Test case for collecting DNS facts from /etc/resolv.conf
def test_collect_dns_facts():
    collector = DnsFactCollector()
    dns_facts = collector.collect()
    
    assert isinstance(dns_facts, dict), "The result should be a dictionary"
    assert 'dns' in dns_facts, "The DNS facts should be under the key 'dns'"
    dns = dns_facts['dns']
    
    # Check nameservers
    if 'nameservers' in dns:
        for ns in dns['nameservers']:
            assert isinstance(ns, str), f"Each nameserver should be a string: {ns}"
    else:
        pytest.fail("Expected key 'nameservers' not found in DNS facts")
    
    # Check domain
    if 'domain' in dns:
        assert isinstance(dns['domain'], str), "The domain should be a string"
    else:
        pytest.fail("Expected key 'domain' not found in DNS facts")
    
    # Check search list
    if 'search' in dns:
        for s in dns['search']:
            assert isinstance(s, str), f"Each item in the search list should be a string: {s}"
    else:
        pytest.fail("Expected key 'search' not found in DNS facts")
    
    # Check sortlist
    if 'sortlist' in dns:
        for sl in dns['sortlist']:
            assert isinstance(sl, str), f"Each item in the sortlist should be a string: {sl}"
    else:
        pytest.fail("Expected key 'sortlist' not found in DNS facts")
    
    # Check options
    if 'options' in dns:
        for opt_key, opt_val in dns['options'].items():
            assert isinstance(opt_key, str), f"Each option key should be a string: {opt_key}"
            assert isinstance(opt_val, (bool, str)), f"Each option value should be a boolean or string: {opt_val}"
    else:
        pytest.fail("Expected key 'options' not found in DNS facts")

# Test case for collecting DNS facts with optional parameters
def test_collect_dns_facts_with_optional_parameters():
    collector = DnsFactCollector()
    dns_facts = collector.collect(module=None, collected_facts=None)
    
    assert isinstance(dns_facts, dict), "The result should be a dictionary"
    assert 'dns' in dns_facts, "The DNS facts should be under the key 'dns'"
    dns = dns_facts['dns']
    
    # Check nameservers
    if 'nameservers' in dns:
        for ns in dns['nameservers']:
            assert isinstance(ns, str), f"Each nameserver should be a string: {ns}"
    else:
        pytest.fail("Expected key 'nameservers' not found in DNS facts")
    
    # Check domain
    if 'domain' in dns:
        assert isinstance(dns['domain'], str), "The domain should be a string"
    else:
        pytest.fail("Expected key 'domain' not found in DNS facts")
    
    # Check search list
    if 'search' in dns:
        for s in dns['search']:
            assert isinstance(s, str), f"Each item in the search list should be a string: {s}"
    else:
        pytest.fail("Expected key 'search' not found in DNS facts")
    
    # Check sortlist
    if 'sortlist' in dns:
        for sl in dns['sortlist']:
            assert isinstance(sl, str), f"Each item in the sortlist should be a string: {sl}"
    else:
        pytest.fail("Expected key 'sortlist' not found in DNS facts")
    
    # Check options
    if 'options' in dns:
        for opt_key, opt_val in dns['options'].items():
            assert isinstance(opt_key, str), f"Each option key should be a string: {opt_key}"
            assert isinstance(opt_val, (bool, str)), f"Each option value should be a boolean or string: {opt_val}"
    else:
        pytest.fail("Expected key 'options' not found in DNS facts")
