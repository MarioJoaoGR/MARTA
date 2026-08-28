
import pytest
from ansible.plugins.callback.minimal import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.inventory.host import Host

@pytest.fixture(scope="module")
def callback_module():
    return CallbackModule()


def test_invalid_input(callback_module):
    with pytest.raises(AttributeError):
        callback_module.v2_runner_on_skipped("invalid input")