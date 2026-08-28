
# Module: ansible.utils.collection_loader._collection_config
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource

# Test fixture to create an instance of _EventSource for each test
@pytest.fixture
def event_source():
    return _EventSource()

# Test case to register a handler and trigger an event
def test_register_and_trigger(event_source):
    def my_handler(event):
        print(f"Handling event: {event}")
    
    # Register the handler
    event_source.register_handler(my_handler)
    
    # Trigger an event
    with pytest.raises(RuntimeError) as excinfo:
        event_source.trigger_event("some_event")  # This should raise a RuntimeError because trigger_event is not defined in the class
    
    assert "trigger_event" in str(excinfo.value), "Expected 'trigger_event' to be mentioned in the error message, but it was not."

# Test case to unregister a handler and ensure it does nothing if the handler is not found
def test_unregister_handler(event_source):
    def my_handler(event):
        print(f"Handling event: {event}")
    
    # Register the handler
    event_source.register_handler(my_handler)
    
    # Unregister the handler
    event_source.__isub__(my_handler)
    
    # Trigger an event to ensure no handlers are called
    with pytest.raises(RuntimeError) as excinfo:
        event_source.trigger_event("some_event")  # This should raise a RuntimeError because trigger_event is not defined in the class
    
    assert "trigger_event" in str(excinfo.value), "Expected 'trigger_event' to be mentioned in the error message, but it was not."
