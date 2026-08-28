
import pytest
from pymonet.task import Task





def test_creating_a_resolved_task():
    resolved_task = Task.of("Success")
    
    def reject(error):
        pytest.fail("This should not be called")
    
    def resolve(result):
        assert result == "Success"
    
    resolved_task.fork(reject, resolve)