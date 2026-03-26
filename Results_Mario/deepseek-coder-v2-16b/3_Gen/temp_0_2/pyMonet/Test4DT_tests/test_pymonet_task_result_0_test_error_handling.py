
import pytest
from pymonet.task import Task

def test_error_handling():
    def handle_success(result):
        assert False, "This should not be called"
    
    def handle_failure(error):
        assert isinstance(error, Exception), "The error should be an instance of Exception"
    
    # Create a Task that will raise an exception during execution
    task = Task(lambda reject, resolve: reject(Exception("Test Error")))
    
    # Execute the task and handle the result or error
    task.fork(handle_failure, handle_success)
