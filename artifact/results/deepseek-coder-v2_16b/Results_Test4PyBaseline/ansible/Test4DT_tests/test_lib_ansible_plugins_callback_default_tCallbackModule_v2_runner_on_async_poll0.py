
import pytest
from ansible.plugins.callback.default import CallbackModule

# Test the initialization of the CallbackModule class
def test_callback_module_initialization():
    callback = CallbackModule()
    assert callback._play is None
    assert callback._last_task_banner is None
    assert callback._last_task_name is None