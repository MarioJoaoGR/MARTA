
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.reboot import ActionModule


@patch('ansible.plugins.action.reboot.ActionBase.__init__', side_effect=TypeError("ActionBase.__init__() missing 6 required positional arguments: 'task', 'connection', 'play_context', 'loader', 'templar', and 'shared_loader_obj'"))
def test_invalid_inputs(*args, **kwargs):
    with pytest.raises(TypeError) as excinfo:
        action_module = ActionModule()
    assert str(excinfo.value) == "ActionBase.__init__() missing 6 required positional arguments: 'task', 'connection', 'play_context', 'loader', 'templar', and 'shared_loader_obj'"
