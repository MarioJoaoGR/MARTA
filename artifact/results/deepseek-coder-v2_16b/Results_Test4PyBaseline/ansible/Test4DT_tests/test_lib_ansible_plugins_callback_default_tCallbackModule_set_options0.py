
import pytest
from ansible.plugins.callback import default

# Import the CallbackModule class from the specified module
CallbackModule = default.CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_default_initialization(callback_module):
    assert isinstance(callback_module, CallbackModule)
    assert callback_module._play is None
    assert callback_module._last_task_banner is None
    assert callback_module._last_task_name is None