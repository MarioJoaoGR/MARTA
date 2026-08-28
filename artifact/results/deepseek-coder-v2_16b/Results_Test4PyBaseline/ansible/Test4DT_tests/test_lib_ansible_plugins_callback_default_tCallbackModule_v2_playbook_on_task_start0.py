# Module: ansible.plugins.callback.default
import pytest
from ansible.plugins.callback import CallbackModule

# Fixture to create an instance of the CallbackModule for testing
@pytest.fixture
def callback_module():
    return CallbackModule()

# Test case to check if the CallbackModule is imported correctly
def test_callback_module_import(callback_module):
    assert isinstance(callback_module, CallbackModule)

# Test case to check initialization of the CallbackModule without parameters
def test_callback_module_initialization():
    callback_module = CallbackModule()
    assert hasattr(callback_module, '_play')
    assert hasattr(callback_module, '_last_task_banner')
    assert hasattr(callback_module, '_last_task_name')
    assert hasattr(callback_module, '_task_type_cache')

# Test case to check the method v2_playbook_on_task_start
def test_v2_playbook_on_task_start(callback_module):
    task = {'name': 'test_task'}
    is_conditional = False
    callback_module.v2_playbook_on_task_start(task, is_conditional)
    assert callback_module._last_task_name == 'test_task'
    assert callback_module._last_task_banner == 'TASK'
