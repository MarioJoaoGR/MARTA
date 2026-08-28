
import pytest
from ansible.plugins.callback.default import CallbackModule

# Test the initialization of the CallbackModule class
def test_callback_module_initialization():
    callback = CallbackModule()
    assert callback._play is None
    assert callback._last_task_banner is None
    assert callback._last_task_name is None
    assert isinstance(callback._task_type_cache, dict)

# Test the v2_runner_on_async_ok method with a mock result object
def test_v2_runner_on_async_ok():
    callback = CallbackModule()
    # Create a mock result object for testing
    class MockResult:
        def __init__(self, host, jid):
            self._host = MockHost(host)
            self._result = {'ansible_job_id': jid}
    
    class MockHost:
        def __init__(self, name):
            self.name = name
        
        def get_name(self):
            return self.name
    
    # Test with a host and job ID
    mock_result = MockResult("example_host", "12345")
    callback.v2_runner_on_async_ok(mock_result)
    assert callback._display.display.call_args[0][0] == "ASYNC OK on example_host: jid=12345"
