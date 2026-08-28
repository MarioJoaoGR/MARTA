
import pytest
from ansible.plugins.lookup.config import _get_global_config
from ansible.errors import AnsibleLookupError, MissingSetting

# Assuming C is an object that has a configuration setting named 'setting_name' with a concrete value
C = type('C', (), {'setting_name': 'value'})()

def test_valid_input():
    result = _get_global_config('setting_name')
    assert result == 'value'

# Assuming C is an object without any configuration settings
C = type('C', (), {})()

def test_missing_setting():
    with pytest.raises(MissingSetting) as excinfo:
        _get_global_config('non_existent_setting')
    assert str(excinfo.value) == "No such config setting 'non_existent_setting' found on C"

# Assuming C has a configuration setting named 'callable_setting' which is a function or method
C = type('C', (), {'callable_setting': lambda: None})()

def test_callable_setting():
    with pytest.raises(AnsibleLookupError) as excinfo:
        _get_global_config('callable_setting')
    assert str(excinfo.value) == 'Invalid setting "callable_setting" attempted'
