# Module: ansible.playbook.play
# test_play.py
from ansible.playbook.play import Play
import pytest

@pytest.fixture
def play():
    return Play()

def test_load_post_tasks_with_valid_data(play):
    # Arrange
    data = {
        'task1': {'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}},
        'task2': {'action': {'module': 'yum', 'args': {'name': 'httpd'}}}
    }
    
    # Act
    play._load_post_tasks('post_tasks', data)
    
    # Assert
    assert len(play.post_tasks) == 2
    assert all(isinstance(task, dict) for task in play.post_tasks)
    assert {'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}} in play.post_tasks
    assert {'name': 'task2', 'action': {'module': 'yum', 'args': {'name': 'httpd'}}} in play.post_tasks

def test_load_post_tasks_with_bare_tasks(play):
    # Arrange
    data = {
        'task1': {'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}},
        'task2': {'action': {'module': 'yum', 'args': {'name': 'httpd'}}}
    }
    
    # Act
    play._load_post_tasks('post_tasks', data)
    
    # Assert
    assert len(play.post_tasks) == 2
    assert all(isinstance(task, dict) for task in play.post_tasks)
    assert {'name': 'task1', 'action': {'module': 'shell', 'args': {'cmd': 'echo Hello'}}} in play.post_tasks
    assert {'name': 'task2', 'action': {'module': 'yum', 'args': {'name': 'httpd'}}} in play.post_tasks

def test_load_post_tasks_with_invalid_data(play):
    # Arrange
    data = {
        'invalid_task': 'not a dictionary'
    }
    
    # Act & Assert
    with pytest.raises(AnsibleParserError):
        play._load_post_tasks('post_tasks', data)
