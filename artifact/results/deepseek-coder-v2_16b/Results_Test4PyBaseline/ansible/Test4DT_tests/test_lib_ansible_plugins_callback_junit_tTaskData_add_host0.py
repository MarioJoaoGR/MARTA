
import pytest
from ansible.plugins.callback import junit

class Host:
    def __init__(self, uuid, status, result):
        self.uuid = uuid
        self.status = status
        self.result = result

def test_taskdata_initialization():
    task = junit.TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='run')
    assert task.uuid == '1234-5678'
    assert task.name == 'ExampleTask'
    assert task.path == '/path/to/task'
    assert task.play is True
    assert task.start is not None
    assert task.action == 'run'

def test_taskdata_initialization_with_specific_values():
    task = junit.TaskData(uuid='1234-5678', name='Task 1', path='/path/to/task', play=True, action='start')
    assert task.uuid == '1234-5678'
    assert task.name == 'Task 1'
    assert task.path == '/path/to/task'
    assert task.play is True
    assert task.start is not None
    assert task.action == 'start'

def test_add_host_to_task():
    task = junit.TaskData(uuid='1234-5678', name='Task 1', path='/path/to/task', play=True, action='start')
    host1 = Host(uuid='host1', status='included', result='Host 1 output')
    task.add_host(host1)
    assert len(task.host_data) == 1
    assert task.host_data['host1'].status == 'included'