
import pytest
from pymonet.task import Task

def my_fork(reject, resolve):
    # Example implementation of a fork function
    pass

@pytest.fixture
def task():
    return Task(my_fork)

def test_bind(task):
    def mapper_function(value):
        return Task(lambda reject, resolve: resolve(value * 2))
    
    new_task = task.bind(mapper_function)
    assert isinstance(new_task, Task)
    # Additional assertions to verify the behavior of bind method can be added here
