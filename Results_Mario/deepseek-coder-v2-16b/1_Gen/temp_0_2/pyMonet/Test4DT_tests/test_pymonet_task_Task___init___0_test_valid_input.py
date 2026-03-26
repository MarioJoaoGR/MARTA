
import pytest
from pymonet.task import Task

def my_fork(reject, resolve):
    pass

@pytest.fixture
def valid_task():
    return Task(my_fork)

def test_valid_input(valid_task):
    assert callable(valid_task.fork)
