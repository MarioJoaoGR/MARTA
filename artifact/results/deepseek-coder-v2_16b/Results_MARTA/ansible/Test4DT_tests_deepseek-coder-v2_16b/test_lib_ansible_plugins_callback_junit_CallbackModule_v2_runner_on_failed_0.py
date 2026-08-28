
import pytest
from ansible.plugins.callback.junit import CallbackModule
import os

@pytest.fixture(scope="module")
def callback_module():
    return CallbackModule()

def test_invalid_input(callback_module):
    with pytest.raises(Exception):
        callback_module.v2_runner_on_failed({'status': 'unknown', 'task_name': 'test_task'})
