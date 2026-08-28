# Module: ansible.plugins.action.copy
# Import the ActionModule class from the correct module
from ansible.plugins.action import ActionModule
import os
import json
import pytest

@pytest.fixture
def action_module():
    # Create an instance of the ActionModule class
    return ActionModule()

@pytest.mark.parametrize("params, expected", [
    ({"src": "local/path/to/file", "dest": "/remote/destination/path"}, {"failed": True, "msg": "src (or content) is required"}),
    ({"content": {'key': 'value'}, "dest": "/remote/destination/path"}, {"failed": False}),
    ({"src": None, "content": {'key': 'value'}, "dest": "/remote/destination/path"}, {"failed": True, "msg": "src and content are mutually exclusive"}),
    ({"content": {'key': 'value'}, "dest": "/remote/destination/path/"}, {"failed": True, "msg": "can not use content with a dir as dest"}),
])
def test_run(action_module, params, expected):
    # Call the run method with parameters and check the result
    try:
        result = action_module.run(**params)
        assert 'failed' in result, "Expected 'failed' key to be in result"
        if 'failed' in result:
            assert result['failed'], "Expected 'failed' to be True"
        if 'msg' in expected:
            assert result['msg'] == expected['msg'], f"Expected msg '{expected['msg']}' but got '{result['msg']}'"
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {str(e)}")
