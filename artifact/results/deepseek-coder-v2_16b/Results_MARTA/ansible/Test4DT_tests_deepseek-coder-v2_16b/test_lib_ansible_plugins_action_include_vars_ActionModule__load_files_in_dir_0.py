
import pytest
from ansible.plugins.action import include_vars
from pathlib import Path
import os

@pytest.fixture(scope="module")
def action_module():
    return include_vars.ActionModule()

# Test Scenario 1: test_valid_input_happy_path
def test_valid_input_happy_path(action_module):
    result = action_module.run(dir='tests/fixtures', depth=1, files_matching='*.yml')
    assert not result['failed'], f"Test failed with error: {result['msg']}"
    assert isinstance(result['files'], dict), "Expected a dictionary of loaded files"

# Test Scenario 2: test_edge_case_none_empty_lists
def test_edge_case_none_empty_lists(action_module):
    result = action_module.run()
    assert not result['failed'], f"Test failed with error: {result['msg']}"
    assert isinstance(result['files'], dict), "Expected a dictionary of loaded files"

# Test Scenario 3: test_invalid_input_error_handling
def test_invalid_input_error_handling(action_module):
    result = action_module.run(dir='nonexistent_directory', depth=1, files_matching='*.yml')
    assert result['failed'], "Expected failure due to invalid directory"
    assert 'msg' in result, "Expected an error message"
    assert "Invalid input: The specified directory does not exist." in result['msg'], "Error message did not match expected content"
