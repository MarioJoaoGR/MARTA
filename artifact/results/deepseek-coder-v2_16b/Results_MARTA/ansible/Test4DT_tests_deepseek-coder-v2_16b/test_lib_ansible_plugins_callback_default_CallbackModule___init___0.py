
import pytest
from ansible.plugins.callback import default

def test_default_callback_instantiation():
    # Instantiate the CallbackModule without any arguments
    callback = default.CallbackModule()
    
    # Assert that the instance was created correctly
    assert isinstance(callback, default.CallbackModule)
    assert callback._play is None
    assert callback._last_task_banner is None
    assert callback._last_task_name is None
    assert isinstance(callback._task_type_cache, dict)

def test_default_callback_init():
    # Instantiate the CallbackModule with None inputs
    callback = default.CallbackModule()
    
    # Assert that the instance was created correctly
    assert isinstance(callback, default.CallbackModule)
    assert callback._play is None
    assert callback._last_task_banner is None
    assert callback._last_task_name is None
    assert isinstance(callback._task_type_cache, dict)
