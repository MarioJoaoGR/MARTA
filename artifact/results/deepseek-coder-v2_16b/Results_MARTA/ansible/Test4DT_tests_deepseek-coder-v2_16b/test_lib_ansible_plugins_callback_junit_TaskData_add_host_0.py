
import pytest
from lib.ansible.plugins.callback import TaskData, HostData

@pytest.fixture
def setup_task():
    return TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')

# Test adding a valid host to the task
def test_valid_input(setup_task):
    task = setup_task
    host = HostData(uuid='new-host-uuid', name='NewHost', status='included', result='initial result')
    task.add_host(host)
    assert task.host_data == {'new-host-uuid': host}

# Test adding a duplicate host to the task and ensure it raises an exception
def test_duplicate_host(setup_task):
    task = setup_task
    host1 = HostData(uuid='existing-host-uuid', name='ExistingHost', status='included', result='initial result')
    task.add_host(host1)
    
    with pytest.raises(Exception, match=r"ExampleTask: True: ExampleTask: duplicate host callback: NewHost"):
        host2 = HostData(uuid='existing-host-uuid', name='NewHost', status='included', result='another result')
        task.add_host(host2)

# Test adding an invalid host (None) to the task and ensure it raises a TypeError
def test_invalid_host(setup_task):
    task = setup_task
    with pytest.raises(TypeError):
        task.add_host(None)
