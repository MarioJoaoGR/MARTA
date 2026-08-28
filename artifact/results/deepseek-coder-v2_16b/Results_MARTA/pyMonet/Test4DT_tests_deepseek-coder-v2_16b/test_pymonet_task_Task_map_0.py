
import pytest
from pymonet.task import Task

# Test valid input scenario
def test_valid_input():
    task = Task(lambda reject, resolve: resolve('success'))
    result = None
    error = None
    try:
        result = task.fork(reject=lambda e: (error := e), resolve=lambda r: (result := r))
    except Exception as e:
        error = e
    
    assert result == 'success'
    assert error is None

# Test edge case scenario with None input
def test_edge_case():
    task = Task(lambda reject, resolve: resolve(None))
    result = None
    error = None
    try:
        result = task.fork(reject=lambda e: (error := e), resolve=lambda r: (result := r))
    except Exception as e:
        error = e
    
    assert result is None
    assert error is None

# Test invalid input scenario raising TypeError
def test_invalid_input():
    task = Task(lambda reject, resolve: resolve('success'))
    with pytest.raises(TypeError):
        task.fork()
