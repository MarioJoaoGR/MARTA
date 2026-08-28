
import pytest
from lib.ansible.module_utils.facts.system.apparmor import ApparmorFactCollector
import os

def test_collect_with_default_parameters():
    collector = ApparmorFactCollector()
    collected_facts = {}
    result = collector.collect(collected_facts=collected_facts)
    assert 'apparmor' in result
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert result['apparmor']['status'] == 'enabled'
    else:
        assert result['apparmor']['status'] == 'disabled'

def test_collect_with_custom_module_parameter():
    collector = ApparmorFactCollector()
    collected_facts = {}
    result = collector.collect(module='custom_module', collected_facts=collected_facts)
    assert 'apparmor' in result
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert result['apparmor']['status'] == 'enabled'
    else:
        assert result['apparmor']['status'] == 'disabled'

def test_collect_with_custom_collected_facts_dictionary():
    collector = ApparmorFactCollector()
    collected_facts = {'additional': 'info'}
    result = collector.collect(collected_facts=collected_facts)
    assert 'apparmor' in result
    if os.path.exists('/sys/kernel/security/apparmor'):
        assert result['apparmor']['status'] == 'enabled'
    else:
        assert result['apparmor']['status'] == 'disabled'
