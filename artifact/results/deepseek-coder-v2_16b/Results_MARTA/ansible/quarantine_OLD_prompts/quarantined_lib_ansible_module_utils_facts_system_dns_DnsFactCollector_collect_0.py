
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.dnsclass import DnsFactCollector

# Test case for collecting DNS facts from /etc/resolv.conf
def test_collect_dns_facts():
    collector = DnsFactCollector()
    
    with patch('builtins.open') as mock_open, \
         patch('os.path.exists', return_value=True), \
         patch('os.access', return_value=True):
        mock_file = MagicMock()
        mock_file.__iter__.return_value = [
            'nameserver 8.8.8.8',
            'nameserver 1.1.1.1',
            'domain example.com',
            'search example.com localdomain',
            'sortlist 192.168.1.1',
            'options timeout 5 attempts 2'
        ]
        
        mock_open.return_value.__enter__.return_value = mock_file
        
        facts = collector.collect()
        
        assert isinstance(facts, dict)
        assert 'dns' in facts
        assert 'nameservers' in facts['dns']
        assert facts['dns']['nameservers'] == ['8.8.8.8', '1.1.1.1']
        assert facts['dns']['domain'] == 'example.com'
        assert facts['dns']['search'] == ['example.com', 'localdomain']
        assert facts['dns']['sortlist'] == ['192.168.1.1']
        assert facts['dns']['options'] == {'timeout': 5, 'attempts': 2}

# Test case for collecting DNS facts with a custom module context
def test_collect_with_module():
    collector = DnsFactCollector()
    
    class MockModule:
        pass
    
    module = MockModule()
    
    with patch('builtins.open') as mock_open, \
         patch('os.path.exists', return_value=True), \
         patch('os.access', return_value=True):
        mock_file = MagicMock()
        mock_file.__iter__.return_value = [
            'nameserver 8.8.8.8',
            'nameserver 1.1.1.1',
            'domain example.com',
            'search example.com localdomain',
            'sortlist 192.168.1.1',
            'options timeout 5 attempts 2'
        ]
        
        mock_open.return_value.__enter__.return_value = mock_file
        
        facts = collector.collect(module=module)
        
        assert isinstance(facts, dict)
        assert 'dns' in facts
        assert 'nameservers' in facts['dns']
        assert facts['dns']['nameservers'] == ['8.8.8.8', '1.1.1.1']
        assert facts['dns']['domain'] == 'example.com'
        assert facts['dns']['search'] == ['example.com', 'localdomain']
        assert facts['dns']['sortlist'] == ['192.168.1.1']
        assert facts['dns']['options'] == {'timeout': 5, 'attempts': 2}

# Test case for collecting DNS facts with custom collected facts storage
def test_collect_with_custom_collected_facts():
    collector = DnsFactCollector()
    
    class MockCollectedFacts:
        pass
    
    collected_facts = MockCollectedFacts()
    
    with patch('builtins.open') as mock_open, \
         patch('os.path.exists', return_value=True), \
         patch('os.access', return_value=True):
        mock_file = MagicMock()
        mock_file.__iter__.return_value = [
            'nameserver 8.8.8.8',
            'nameserver 1.1.1.1',
            'domain example.com',
            'search example.com localdomain',
            'sortlist 192.168.1.1',
            'options timeout 5 attempts 2'
        ]
        
        mock_open.return_value.__enter__.return_value = mock_file
        
        facts = collector.collect(collected_facts=collected_facts)
        
        assert isinstance(facts, dict)
        assert 'dns' in facts
        assert 'nameservers' in facts['dns']
        assert facts['dns']['nameservers'] == ['8.8.8.8', '1.1.1.1']
        assert facts['dns']['domain'] == 'example.com'
        assert facts['dns']['search'] == ['example.com', 'localdomain']
        assert facts['dns']['sortlist'] == ['192.168.1.1']
        assert facts['dns']['options'] == {'timeout': 5, 'attempts': 2}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_module_utils_facts_system_dns_DnsFactCollector_collect_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_dns_DnsFactCollector_collect_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_dns_DnsFactCollector_collect_0.py:4: in <module>
    from ansible.module_utils.facts.system.dnsclass import DnsFactCollector
E   ModuleNotFoundError: No module named 'ansible.module_utils.facts.system.dnsclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_dns_DnsFactCollector_collect_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.40s ===============================
"""