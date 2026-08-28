
import pytest
from ansible.plugins.action.reboot import ActionModule



def test_invalid_inputs():
    with pytest.raises(TypeError):
        action_module = ActionModule()