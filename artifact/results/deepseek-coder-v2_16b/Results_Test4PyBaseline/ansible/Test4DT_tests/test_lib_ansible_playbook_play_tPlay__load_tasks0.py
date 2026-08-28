# Module: ansible.playbook.play
# test_play.py
from your_module import Play

def test_basic_play_configuration():
    play = Play()
    assert play._hosts == []
    assert play._gather_facts is None
    assert play._tasks == []
    assert play._roles == []

def test_play_with_variable_files_and_gather_facts():
    play = Play()
    play._hosts = ['host3', 'host4']
    play._gather_facts = True
    play._tasks.append({'name': 'task2', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}})
    play._vars_files = ['/path/to/var1.yml', '/path/to/var2.yml']
    play._roles.append('role2')
    
    assert play._hosts == ['host3', 'host4']
    assert play._gather_facts is True
    assert len(play._tasks) == 1
    assert len(play._vars_files) == 2
    assert len(play._roles) == 1

def test_play_with_handlers_and_serial_strategy():
    play = Play()
    play._hosts = ['host5', 'host6']
    play._tasks.append({'name': 'task3', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}})
    play._force_handlers = True
    play._serial = ['task1']
    play._roles.append('role3')
    
    assert play._hosts == ['host5', 'host6']
    assert play._force_handlers is True
    assert len(play._serial) == 1
    assert len(play._roles) == 1

def test_play_with_max_fail_percentage_and_strategy():
    play = Play()
    play._hosts = ['host7', 'host8']
    play._tasks.append({'name': 'task4', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}})
    play._max_fail_percentage = 20
    play._strategy = 'free'
    play._roles.append('role4')
    
    assert play._hosts == ['host7', 'host8']
    assert play._max_fail_percentage == 20
    assert play._strategy == 'free'
    assert len(play._roles) == 1

def test_play_with_pre_and_post_tasks():
    play = Play()
    play._hosts = ['host9', 'host10']
    play._pre_tasks.append({'name': 'pre_task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Pre'}}})
    play._tasks.append({'name': 'main_task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Main'}}})
    play._post_tasks.append({'name': 'post_task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Post'}}})
    play._roles.append('role5')
    
    assert len(play._pre_tasks) == 1
    assert len(play._tasks) == 1
    assert len(play._post_tasks) == 1
    assert len(play._roles) == 1
