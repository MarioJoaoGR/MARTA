
import pytest
from ansible.plugins.callback import default

# Assuming 'callback_module' is an instance of CallbackModule
@pytest.fixture
def callback_module():
    return default.CallbackModule()

# Define a sample task dictionary for a cleanup task
@pytest.fixture
def task():
    return {"name": "Cleanup Task", "type": "cleanup"}

def test_v2_playbook_on_cleanup_task_start(callback_module, task):
    # Call the method with the instantiated callback module and the task dictionary
    callback_module.v2_playbook_on_cleanup_task_start(task)
    
    # Add assertions to validate the expected behavior
    assert callback_module._last_task_name == "Cleanup Task"
    assert callback_module._last_task_banner == 'CLEANUP TASK'
