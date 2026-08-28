
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource

# Test fixture to create an instance of _EventSource for each test
@pytest.fixture
def event_source():
    return _EventSource()

# Test case to ensure that the method returns self after attempting to remove a non-existent handler
def test_remove_non_existent_handler(event_source):
    initial_handlers = len(event_source._handlers)
    handler = lambda event: print(f"Handling event: {event}")
    
    # Attempt to remove a non-existent handler
    event_source.__isub__(handler)
    
    # Check that the number of handlers remains unchanged and the method returns self
    assert len(event_source._handlers) == initial_handlers
    assert event_source is not None  # Assuming __isub__ returns 'self'

# Test case to ensure that attempting to remove a non-existent handler does not raise an error
def test_remove_non_existent_handler_no_error(event_source):
    handler = lambda event: print(f"Handling event: {event}")
    
    # Attempt to remove a non-existent handler without raising an error
    event_source.__isub__(handler)
    
    # Check that the number of handlers remains unchanged and no exception was raised
    assert len(event_source._handlers) == 0

# Test case to ensure that attempting to remove a non-existent handler does not raise an error even if called multiple times
def test_remove_non_existent_handler_multiple_calls(event_source):
    handler = lambda event: print(f"Handling event: {event}")
    
    # Call __isub__ multiple times with the same non-existent handler
    for _ in range(5):
        event_source.__isub__(handler)
    
    # Check that the number of handlers remains unchanged and no exception was raised
    assert len(event_source._handlers) == 0
