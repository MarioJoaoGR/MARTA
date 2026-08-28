# Module: ansible.playbook.play
# test_play.py
from your_module import Play  # Replace 'your_module' with the actual module where Play is defined

def test_basic_play_configuration():
    play = Play()
    play._hosts = ['host1', 'host2']
    play._gather_facts = True
    task = {'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}}
    play._tasks.append(task)
    play._roles.append('role1')
    
    assert play._hosts == ['host1', 'host2']
    assert play._gather_facts is True
    assert len(play._tasks) == 1
    assert play._tasks[0]['name'] == 'task1'
    assert play._roles == ['role1']

def test_play_configuration_with_variable_files_and_prompt_variables():
    play = Play()
    play._hosts = ['host1', 'host2']
    play._gather_facts = True
    task = {'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}}
    play._tasks.append(task)
    play._vars_files = ['file1.yml', 'file2.yml']
    play._vars_prompt = [{'name': 'var1', 'prompt': 'Enter value for var1'}, {'name': 'var2', 'prompt': 'Enter value for var2'}]
    
    assert len(play._vars_files) == 2
    assert len(play._vars_prompt) == 2

def test_play_configuration_with_serial_execution_and_strategy():
    play = Play()
    play._hosts = ['host1', 'host2']
    play._gather_facts = True
    task = {'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}}
    play._tasks.append(task)
    play._serial = ['host1']
    play._strategy = 'linear'
    
    assert play._serial == ['host1']
    assert play._strategy == 'linear'

def test_play_configuration_with_force_handlers_and_max_fail_percentage():
    play = Play()
    play._hosts = ['host1', 'host2']
    play._gather_facts = True
    task = {'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}}
    play._tasks.append(task)
    play._force_handlers = True
    play._max_fail_percentage = 10
    
    assert play._force_handlers is True
    assert play._max_fail_percentage == 10
