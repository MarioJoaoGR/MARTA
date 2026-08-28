
# Module: ansible.utils.collection_loader._collection_config
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource

# Test fixture to create an instance of _EventSource for each test
@pytest.fixture
def event_source():
    return _EventSource()

# Test case to check if the handler is registered correctly
def test_register_handler(event_source):
    def my_handler(event):
        print(f"Handling event: {event}")
    
    # Using __iadd__ method to add handlers
    event_source += my_handler
    assert len(event_source._handlers) == 1

# Additional test case to check if adding a non-callable raises ValueError
def test_non_callable_handler():
    event_source = _EventSource()
    with pytest.raises(ValueError):
        event_source += "not callable"
    assert len(event_source._handlers) == 0
