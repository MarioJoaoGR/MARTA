
import pytest
from ansible.plugins.action import unarchive
from unittest.mock import patch, MagicMock

@pytest.fixture
def valid_instance():
    action = unarchive.ActionModule()
    task_vars = {
        'src': '/path/to/source.zip',
        'dest': '/destination/directory',
        'remote_src': False,
        'creates': None,
        'decrypt': True
    }
    action._task.args = MagicMock(return_value=task_vars)
    return action

@pytest.fixture
def edge_case_instance():
    action = unarchive.ActionModule()
    task_vars = {
        'src': None,
        'dest': '',
        'remote_src': True,
        'creates': None,
        'decrypt': False
    }
    action._task.args = MagicMock(return_value=task_vars)
    return action

@pytest.fixture
def invalid_instance():
    action = unarchive.ActionModule()
    task_vars = {
        'src': '/path/to/invalid',
        'dest': 123,
        'remote_src': None,
        'creates': 'non_existent_file',
        'decrypt': True
    }
    action._task.args = MagicMock(return_value=task_vars)
    return action

def test_valid_inputs(valid_instance):
    with patch('ansible.plugins.action.unarchive.os.path') as mock_os_path:
        mock_os_path.expanduser.return_value = '/expanded/source'
        result = valid_instance.run()
        assert 'dest' in result, "Expected 'dest' to be in the result"
        assert result['dest'] == '/destination/directory', "Expected destination directory to match"

def test_edge_cases(edge_case_instance):
    with patch('ansible.plugins.action.unarchive.os.path') as mock_os_path:
        edge_case_instance._task.args = MagicMock(return_value={})
        result = edge_case_instance.run()
        assert 'error' in result, "Expected an error to be present"
        assert 'msg' in result['error'], "Expected the error message to be present"

def test_invalid_inputs(invalid_instance):
    with pytest.raises(Exception) as e:
        invalid_instance.run()
        assert str(e) == "src (or content) and dest are required", "Expected specific error message for invalid inputs"
