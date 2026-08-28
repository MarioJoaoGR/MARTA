# Module: ansible.playbook.play
# test_play.py
from ansible.playbook.play import Play
import pytest

@pytest.fixture
def create_play():
    def _create_play(**kwargs):
        play = Play()
        for attr, value in kwargs.items():
            setattr(play, f"_{attr}", value)
        return play
    return _create_play

# Test creating a basic Play object
def test_basic_play_creation(create_play):
    play = create_play()
    assert hasattr(play, '_hosts')
    assert hasattr(play, '_gather_facts')
    assert hasattr(play, '_gather_subset')
    assert hasattr(play, '_gather_timeout')
    assert hasattr(play, '_fact_path')
    assert hasattr(play, '_vars_files')
    assert hasattr(play, '_vars_prompt')
    assert hasattr(play, '_roles')
    assert hasattr(play, '_handlers')
    assert hasattr(play, '_pre_tasks')
    assert hasattr(play, '_post_tasks')
    assert hasattr(play, '_tasks')
    assert hasattr(play, '_force_handlers')
    assert hasattr(play, '_max_fail_percentage')
    assert hasattr(play, '_serial')
    assert hasattr(play, '_strategy')
    assert hasattr(play, '_order')

# Test setting and getting attributes of Play object
def test_set_and_get_attributes(create_play):
    play = create_play()
    hosts = ['host1', 'host2']
    gather_facts = True
    gather_subset = ['all']
    gather_timeout = 30
    roles = [{'name': 'role1'}, {'name': 'role2'}]
    
    play._hosts = hosts
    play._gather_facts = gather_facts
    play._gather_subset = gather_subset
    play._gather_timeout = gather_timeout
    play._roles = roles
    
    assert play._hosts == hosts
    assert play._gather_facts == gather_facts
    assert play._gather_subset == gather_subset
    assert play._gather_timeout == gather_timeout
    assert play._roles == roles

# Test loading roles into a Play object
def test_load_roles(create_play):
    play = create_play()
    ds = [{'name': 'role1'}, {'name': 'role2'}]
    roles = play._load_roles('roles', ds)
    
    assert len(roles) == 2
    assert all([isinstance(r, Role) for r in roles])

# Test edge case where datastructure is None
def test_load_roles_with_none_datastructure(create_play):
    play = create_play()
    ds = None
    roles = play._load_roles('roles', ds)
    
    assert len(roles) == 0
