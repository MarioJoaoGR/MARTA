
# Module: ansible.plugins.callback.default
# test_default_callback.py
from ansible.plugins.callback import default
import pytest

@pytest.fixture
def callback_module():
    return default.CallbackModule()

def test_v2_runner_on_unreachable(callback_module, capsys):
    # Create a mock result object with the necessary structure for v2_runner_on_unreachable method
    class MockResult:
        def __init__(self, task, status, error):
            self._task = task
            self.status = status
            self._result = {'error': error}
    
    # Create a mock task object (you can customize this as needed)
    class MockTask:
        def __init__(self, uuid):
            self._uuid = uuid
    
    # Test with a different result
    test_task = MockTask("different_task_uuid")
    test_result = MockResult(test_task, "unreachable", "Another reason for unreachability")
    
    callback_module.v2_runner_on_unreachable(test_result)
    captured = capsys.readouterr()
    assert captured.out == "fatal: []: UNREACHABLE! => {'error': 'Another reason for unreachability', 'status': 'unreachable'}\n"
