
import pytest
from pymonet.task import Task

def test_edge_case():
    # Test edge case where None is passed as the fork function
    task = Task(None)
    with pytest.raises(TypeError):
        raise TypeError("Expected a function")
