# Module: ansible.plugins.callback.default
import pytest
from ansible.plugins.callback import default as callback_module

# Initialize the callback module instance
callback = callback_module.CallbackModule()

def test_initialization():
    assert isinstance(callback, callback_module.CallbackModule)

@pytest.mark.parametrize("result", [
    type('Result', (object,), {'_host': type('Host', (object,), {'get_name': lambda self: 'localhost'})(), '_task': type('Task', (object,), {'action': 'some_action'})(), '_result': {'failed': True}})()
])
def test_v2_runner_on_failed(result):
    with pytest.raises(SystemExit) as excinfo:
        callback.v2_runner_on_failed(result)
    assert "fatal: [localhost]: FAILED! => {'failed': True}" in str(excinfo.value)

@pytest.mark.parametrize("result, ignore_errors", [
    (type('Result', (object,), {'_host': type('Host', (object,), {'get_name': lambda self: 'localhost'})(), '_task': type('Task', (object,), {'action': 'some_action'})(), '_result': {'failed': True}})(), False),
    (type('Result', (object,), {'_host': type('Host', (object,), {'get_name': lambda self: 'localhost'})(), '_task': type('Task', (object,), {'action': 'some_action'})(), '_result': {'failed': True}})(), True)
])
def test_v2_runner_on_failed_with_ignore_errors(result, ignore_errors):
    if ignore_errors:
        callback.v2_runner_on_failed(result, ignore_errors=True)
    else:
        with pytest.raises(SystemExit) as excinfo:
            callback.v2_runner_on_failed(result)
        assert "fatal: [localhost]: FAILED! => {'failed': True}" in str(excinfo.value)
