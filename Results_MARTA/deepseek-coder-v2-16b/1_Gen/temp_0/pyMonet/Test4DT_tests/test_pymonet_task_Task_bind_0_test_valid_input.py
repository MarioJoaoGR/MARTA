
import pytest
from pymonet.task import Task

def my_fork(reject, resolve):
    return 'resolved'

@pytest.fixture
def task():
    return Task(my_fork)

def test_valid_input(task):
    def mapper_fn(value):
        return Task(lambda reject, resolve: resolve(value * 2))
    
    new_task = task.bind(mapper_fn)
    assert new_task.fork(lambda err: None, lambda val: val) == 'resolved'
