
import pytest
from pymonet.task import Task

def my_fork(reject, resolve):
    # Example implementation of a fork function
    pass

@pytest.fixture
def task():
    return Task(my_fork)

def test_edge_case(task):
    # Test None input
    with pytest.raises(TypeError):
        task.bind(lambda x: x)(None, lambda x: x)
    
    # Test empty function
    def empty_function():
        pass
    assert task.bind(empty_function).fork(lambda _: 'reject', lambda _: 'resolve') == Task(my_fork).fork(lambda _: 'reject', lambda _: 'resolve')
