
import pytest
from your_module import _EventSource  # Assuming this is part of a module named 'your_module'

# Test adding a valid handler function
def test_valid_add_handler():
    event_source = _EventSource()
    
    def handle1():
        print("Handler 1")
    
    event_source.add_handler(handle1)
    assert len(event_source._handlers) == 1
    assert handle1 in event_source._handlers

# Test adding an invalid handler and expect ValueError
def test_invalid_add_handler():
    event_source = _EventSource()
    
    handle2 = None
    with pytest.raises(ValueError):
        event_source.add_handler(handle2)

# Test removing a non-existent handler and ensure no error occurs
def test_invalid_remove_handler():
    event_source = _EventSource()
    
    def handle3():
        print("Handler 3")
    
    event_source.add_handler(handle3)
    assert len(event_source._handlers) == 1
    assert handle3 in event_source._handlers
    
    event_source.remove_handler(lambda: None)
    assert len(event_source._handlers) == 1
