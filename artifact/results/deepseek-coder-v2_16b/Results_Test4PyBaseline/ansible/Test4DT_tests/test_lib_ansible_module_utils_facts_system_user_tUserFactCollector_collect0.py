# Module: ansible.module_utils.facts.system.user
import pytest
from ansible.module_utils.facts.system.user import UserFactCollector
import getpass
import pwd
import os

# Test default initialization and collection
def test_default_initialization_and_collection():
    collector = UserFactCollector()
    user_facts = collector.collect()
    
    assert 'user_id' in user_facts
    assert isinstance(user_facts['user_id'], str)
    
    assert 'user_uid' in user_facts
    assert isinstance(user_facts['user_uid'], int)
    
    assert 'user_gid' in user_facts
    assert isinstance(user_facts['user_gid'], int)
    
    assert 'user_gecos' in user_facts
    assert isinstance(user_facts['user_gecos'], str)
    
    assert 'user_dir' in user_facts
    assert isinstance(user_facts['user_dir'], str)
    
    assert 'user_shell' in user_facts
    assert isinstance(user_facts['user_shell'], str)
    
    assert 'real_user_id' in user_facts
    assert isinstance(user_facts['real_user_id'], int)
    
    assert 'effective_user_id' in user_facts
    assert isinstance(user_facts['effective_user_id'], int)
    
    assert 'effective_group_id' in user_facts
    assert isinstance(user_facts['effective_group_id'], int)

# Test collection with a mock module
class MockModule:
    def __init__(self):
        self.params = {}

def test_collection_with_mock_module():
    collector = UserFactCollector(module=MockModule(), collected_facts={})
    user_facts = collector.collect()
    
    assert 'user_id' in user_facts
    assert isinstance(user_facts['user_id'], str)
    
    assert 'user_uid' in user_facts
    assert isinstance(user_facts['user_uid'], int)
    
    assert 'user_gid' in user_facts
    assert isinstance(user_facts['user_gid'], int)
    
    assert 'user_gecos' in user_facts
    assert isinstance(user_facts['user_gecos'], str)
    
    assert 'user_dir' in user_facts
    assert isinstance(user_facts['user_dir'], str)
    
    assert 'user_shell' in user_facts
    assert isinstance(user_facts['user_shell'], str)
    
    assert 'real_user_id' in user_facts
    assert isinstance(user_facts['real_user_id'], int)
    
    assert 'effective_user_id' in user_facts
    assert isinstance(user_facts['effective_user_id'], int)
    
    assert 'effective_group_id' in user_facts
    assert isinstance(user_facts['effective_group_id'], int)

# Test collection with a real module
class RealModule:
    def __init__(self):
        self.params = {}

def test_collection_with_real_module():
    collector = UserFactCollector(module=RealModule(), collected_facts={})
    user_facts = collector.collect()
    
    assert 'user_id' in user_facts
    assert isinstance(user_facts['user_id'], str)
    
    assert 'user_uid' in user_facts
    assert isinstance(user_facts['user_uid'], int)
    
    assert 'user_gid' in user_facts
    assert isinstance(user_facts['user_gid'], int)
    
    assert 'user_gecos' in user_facts
    assert isinstance(user_facts['user_gecos'], str)
    
    assert 'user_dir' in user_facts
    assert isinstance(user_facts['user_dir'], str)
    
    assert 'user_shell' in user_facts
    assert isinstance(user_facts['user_shell'], str)
    
    assert 'real_user_id' in user_facts
    assert isinstance(user_facts['real_user_id'], int)
    
    assert 'effective_user_id' in user_facts
    assert isinstance(user_facts['effective_user_id'], int)
    
    assert 'effective_group_id' in user_facts
    assert isinstance(user_facts['effective_group_id'], int)
