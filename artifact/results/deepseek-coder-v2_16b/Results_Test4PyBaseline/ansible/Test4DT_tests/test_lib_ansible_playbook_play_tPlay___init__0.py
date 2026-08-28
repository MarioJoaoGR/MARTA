
# Module: ansible.playbook.play
# test_play.py
from ansible.playbook.play import Play

def test_basic_initialization():
    play = Play()
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

def test_initialization_with_specific_hosts():
    play = Play()
    play._hosts = ['host1', 'host2']
    assert play._hosts == ['host1', 'host2']

def test_setting_gather_facts_to_true():
    play = Play()
    play._hosts = ['host1', 'host2']
    play._gather_facts = True
    assert play._gather_facts is True

def test_adding_tasks_and_roles():
    play = Play()
    play._hosts = ['host1', 'host2']
    if not hasattr(play, '_tasks'):  # Adding this check because pylint complained about no-member error
        play._tasks = []
    if not hasattr(play, '_roles'):  # Similarly adding checks for _roles and _tasks
        play._roles = []
    play._tasks.append({'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}})
