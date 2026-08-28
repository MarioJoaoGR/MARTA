
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.plugins.callback import TaskData, HostData

# Test Case 1: Basic Initialization of TaskData
def test_taskdata_initialization():
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    assert task.uuid == '1234-5678'
    assert task.name == 'ExampleTask'
    assert task.play is True
    assert task.action == 'start'

# Test Case 2: Initialization with Specific Values
def test_taskdata_initialization_with_specific_values():
    task = TaskData(uuid='5678-1234', name='AnotherTask', path='/another/path/to/task', play=False, action='pause')
    assert task.uuid == '5678-1234'
    assert task.name == 'AnotherTask'
    assert task.play is False
    assert task.action == 'pause'

# Test Case 3: Adding a Host to the Task
@patch('lib.ansible.plugins.callback.TaskData.HostData', autospec=True)
def test_add_host(mock_hostdata):
    mock_host = MagicMock()
    mock_host.uuid = 'uuid123'
    mock_host.status = 'included'
    mock_host.result = 'initial result'
    
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    task.add_host(mock_host)
    assert mock_host in task.host_data.values()

# Test Case 4: Handling Duplicate Hosts
@patch('lib.ansible.plugins.callback.TaskData.HostData', autospec=True)
def test_duplicate_host_exception(mock_hostdata):
    mock_host1 = MagicMock()
    mock_host1.uuid = 'uuid123'
    mock_host1.status = 'included'
    mock_host1.result = 'result from host1'
    
    task = TaskData(uuid='1234-5678', name='ExampleTask', path='/path/to/task', play=True, action='start')
    task.add_host(mock_host1)  # Adding the first host

    mock_host2 = MagicMock()
    mock_host2.uuid = 'uuid123'
    mock_host2.status = 'included'
    mock_host2.result = 'result from host2'
    
    with pytest.raises(Exception) as excinfo:
        task.add_host(mock_host2)  # Attempting to add a duplicate host will raise an Exception
    
    assert str(excinfo.value) == f"{'/path/to/task': %s: ExampleTask: duplicate host callback: uuid123" % ('True',)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: f-string: expecting '}' (line 53, col 105)
    assert str(excinfo.value) == f"{'/path/to/task': %s: ExampleTask: duplicate host callback: uuid123" % ('True',)
"""