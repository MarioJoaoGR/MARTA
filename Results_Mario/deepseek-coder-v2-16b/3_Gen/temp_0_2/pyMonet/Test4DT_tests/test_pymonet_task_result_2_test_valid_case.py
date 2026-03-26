
import pytest
from pymonet.task import Task

def handle_success(result):
    print("Success:", result)

def handle_failure(error):
    print("Failure:", error)

@pytest.fixture
def task():
    # Assuming `computation` is a function that returns a Result object
    def computation():
        return Task(lambda reject, resolve: resolve("success"))
    
    return computation()

def test_valid_case(task):
    task.fork(handle_failure, handle_success)
    # Add assertions or checks here to verify the expected behavior
