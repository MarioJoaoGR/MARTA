# Module: ansible.plugins.callback.default
import pytest
from ansible.plugins.callback import default

# Import the CallbackModule class from the provided module name
CallbackModule = default.CallbackModule

def test_callbackmodule_initialization():
    """Test that the CallbackModule can be initialized without any parameters."""
    callback_module = CallbackModule()
    assert isinstance(callback_module, CallbackModule)

def test_callbackmodule_attributes():
    """Test that the CallbackModule has the expected attributes after initialization."""
    callback_module = CallbackModule()
    assert hasattr(callback_module, '_play')
    assert hasattr(callback_module, '_last_task_banner')
    assert hasattr(callback_module, '_last_task_name')
    assert hasattr(callback_module, '_task_type_cache')
