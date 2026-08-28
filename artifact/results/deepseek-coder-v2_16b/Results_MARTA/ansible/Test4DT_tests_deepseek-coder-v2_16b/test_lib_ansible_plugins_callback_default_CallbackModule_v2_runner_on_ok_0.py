
import pytest
from ansible.plugins.callback import default

class CallbackModule(default.CallbackModule):
    def __init__(self):
        super(CallbackModule, self).__init__()

def test_valid_input():
    callback_module = CallbackModule()
    result = {'_task': 'some_task', '_result': {'changed': True}}
    with pytest.raises(AttributeError):
        callback_module.v2_runner_on_ok(result)
