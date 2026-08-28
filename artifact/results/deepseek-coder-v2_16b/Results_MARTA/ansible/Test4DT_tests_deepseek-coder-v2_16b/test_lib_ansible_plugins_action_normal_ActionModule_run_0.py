
import pytest
from ansible.plugins.action import normal

@pytest.fixture(scope="module")
def action_module():
    return normal.ActionModule()

# Test Scenario 1: test_valid_inputs
def test_valid_inputs(action_module):
    result = action_module.run()
    assert 'skipped' not in result, "Expected 'skipped' to be False"
    assert 'invocation' in result, "Expected 'invocation' key in result"
    assert 'module_args' not in result['invocation'], "Expected 'module_args' to be removed"

# Test Scenario 2: test_edge_cases
def test_edge_cases(action_module):
    # Test with None parameters
    result = action_module.run(tmp=None, task_vars=None)
    assert 'skipped' not in result, "Expected 'skipped' to be False"
    assert 'invocation' in result, "Expected 'invocation' key in result"
    assert 'module_args' not in result['invocation'], "Expected 'module_args' to be removed"
    
    # Test with empty lists and dictionaries
    result = action_module.run(tmp={}, task_vars={})
    assert 'skipped' not in result, "Expected 'skipped' to be False"
    assert 'invocation' in result, "Expected 'invocation' key in result"
    assert 'module_args' not in result['invocation'], "Expected 'module_args' to be removed"

# Test Scenario 3: test_invalid_inputs
def test_invalid_inputs(action_module):
    # Test with incorrect parameter types
    with pytest.raises(TypeError):
        action_module.run(tmp="string", task_vars=123)
    
    # Test with invalid values for parameters
    with pytest.raises(ValueError):
        action_module.run(tmp={'invalid': 'data'}, task_vars={'invalid': 'data'})
