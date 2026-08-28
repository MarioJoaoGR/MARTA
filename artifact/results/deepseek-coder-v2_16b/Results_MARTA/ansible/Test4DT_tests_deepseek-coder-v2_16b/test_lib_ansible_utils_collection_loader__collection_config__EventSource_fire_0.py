
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource

# Test adding a handler

# Test removing a handler

# Test triggering an event with no handlers
def test_trigger_event_no_handlers():
    event_source = _EventSource()
    
    with pytest.raises(AttributeError):
        event_source.trigger_event()

# Test triggering an event with multiple handlers

# Test firing an event and handling exceptions in handlers