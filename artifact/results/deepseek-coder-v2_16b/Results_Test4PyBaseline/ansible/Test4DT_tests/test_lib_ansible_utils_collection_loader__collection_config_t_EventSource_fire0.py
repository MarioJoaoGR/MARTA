# Module: ansible.utils.collection_loader._collection_config
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource

# Test initialization of EventSource
def test__init__():
    event_source = _EventSource()
    assert hasattr(event_source, '_handlers'), "EventSource should have a _handlers attribute"
    assert isinstance(event_source._handlers, set), "_handlers should be a set"

# Test registering and triggering an event with one handler
def test_register_and_trigger_one_handler():
    event_source = _EventSource()
    
    def my_handler(event):
        assert event == "some_event", "Handler should receive the triggered event"
    
    event_source.register_handler(my_handler)
    event_source.trigger_event("some_event")

# Test registering and triggering an event with multiple handlers
def test_register_and_trigger_multiple_handlers():
    event_source = _EventSource()
    
    def handler1(event):
        assert False, "handler1 should not be called"
    
    def handler2(event):
        assert event == "some_event", "Handler should receive the triggered event"
    
    event_source.register_handler(handler1)
    event_source.register_handler(handler2)
    event_source.trigger_event("some_event")

# Test unregistering a handler
def test_unregister_handler():
    event_source = _EventSource()
    
    def my_handler(event):
        assert False, "my_handler should not be called"
    
    event_source.register_handler(my_handler)
    event_source.unregister_handler(my_handler)
    event_source.trigger_event("some_event")  # No handlers should handle this event

# Test handling an exception within a handler
def test_handle_exception():
    event_source = _EventSource()
    
    def handle_exception(exc, exc_type, *args, **kwargs):
        assert isinstance(exc, ValueError), "Handler should receive the raised exception"
        return False  # Return False to continue execution
    
    event_source._handlers.add(handle_exception)
    
    with pytest.raises(ValueError):
        raise ValueError("Test exception")

# Test re-raising an exception if _on_exception returns True
def test_reraise_exception():
    event_source = _EventSource()
    
    def handle_exception(exc, exc_type, *args, **kwargs):
        assert isinstance(exc, ValueError), "Handler should receive the raised exception"
        return True  # Return True to re-raise the exception
    
    event_source._handlers.add(handle_exception)
    
    with pytest.raises(ValueError):
        raise ValueError("Test exception")
