
import pytest
from pymonet.task import Task

def test_edge_case():
    # Test None value
    task_none = Task.of(None)
    assert task_none.fork(lambda _: "Should not be called", lambda x: str(x)) == "None"
    
    # Test empty string value
    task_empty_string = Task.of("")
    assert task_empty_string.fork(lambda _: "Should not be called", lambda x: str(x)) == ""
    
    # Test zero value
    task_zero = Task.of(0)
    assert task_zero.fork(lambda _: "Should not be called", lambda x: str(x)) == "0"
