
import pytest
from pymonet.task import Task

@pytest.fixture
def task():
    def my_fork(reject, resolve):
        # Example implementation of a fork function
        pass
    return Task(my_fork)

def test_valid_inputs(task):
    assert isinstance(task, Task)
