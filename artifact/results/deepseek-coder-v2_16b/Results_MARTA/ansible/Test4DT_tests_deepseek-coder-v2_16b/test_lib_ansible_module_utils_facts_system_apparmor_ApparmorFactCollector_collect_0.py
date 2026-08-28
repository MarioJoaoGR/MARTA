
import pytest
from lib.ansible.module_utils.facts.system.apparmor import ApparmorFactCollector
import os


def test_default_parameters():
    collector = ApparmorFactCollector()
    collected_facts = {}
    result = collector.collect(collected_facts=collected_facts)
    assert 'apparmor' in result, "Expected 'apparmor' key to be in the result dictionary."
    assert result['apparmor']['status'] == 'enabled' if os.path.exists('/sys/kernel/security/apparmor') else 'disabled', f"Expected status to be {'enabled' if os.path.exists('/sys/kernel/security/apparmor') else 'disabled'} but got {result['apparmor']['status']}."

def test_custom_module_parameter():
    collector = ApparmorFactCollector()
    collected_facts = {}
    result = collector.collect(module='custom_module', collected_facts=collected_facts)
    assert 'apparmor' in result, "Expected 'apparmor' key to be in the result dictionary."
    assert result['apparmor']['status'] == 'enabled' if os.path.exists('/sys/kernel/security/apparmor') else 'disabled', f"Expected status to be {'enabled' if os.path.exists('/sys/kernel/security/apparmor') else 'disabled'} but got {result['apparmor']['status']}."

def test_custom_collected_facts():
    collector = ApparmorFactCollector()
    collected_facts = {'additional': 'info'}
    result = collector.collect(collected_facts=collected_facts)
    assert 'apparmor' in result, "Expected 'apparmor' key to be in the result dictionary."
    assert result['apparmor']['status'] == 'enabled' if os.path.exists('/sys/kernel/security/apparmor') else 'disabled', f"Expected status to be {'enabled' if os.path.exists('/sys/kernel/security/apparmor') else 'disabled'} but got {result['apparmor']['status']}."