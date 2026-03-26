
import pytest
from pymonet.task import Task

def test_none_input():
    # Test when fork is None
    task = Task(None)
    assert task.fork is None
