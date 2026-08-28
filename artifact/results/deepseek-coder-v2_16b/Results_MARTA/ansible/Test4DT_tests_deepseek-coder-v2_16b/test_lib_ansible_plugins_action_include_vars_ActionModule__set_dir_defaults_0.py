
import pytest
import re
from ansible.plugins.action import include_vars

@pytest.fixture
def action_module():
    return include_vars._set_dir_defaults()

def test_default_values(action_module):
    assert action_module.depth == 0
    assert action_module.matcher is None
    assert action_module.ignore_files == []

def test_custom_values(action_module):
    action_module.depth = 2
    action_module.files_matching = '*.txt'
    action_module._set_dir_defaults()
    assert action_module.depth == 2
    assert re.match('*.txt', action_module.matcher.pattern) is not None
    assert isinstance(action_module.ignore_files, list)

def test_invalid_inputs(action_module):
    action_module.depth = None
    action_module.files_matching = None
    action_module._set_dir_defaults()
    assert action_module.depth == 0
    assert action_module.matcher is None
    assert isinstance(action_module.ignore_files, list)
