
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource

def test__add_handler():
    event_source = _EventSource()
    
    def handle1():
        pass
    
    with pytest.raises(AttributeError):
        event_source.add_handler(handle1)

def test__remove_handler():
    event_source = _EventSource()
    
    def handle1():
        pass
    
    with pytest.raises(AttributeError):
        event_source.add_handler(handle1)
        event_source.remove_handler(handle1)

def test__trigger_event():
    event_source = _EventSource()
    
    def handle1():
        print("Handler 1")
    
    def handle2():
        print("Handler 2")
    
    with pytest.raises(AttributeError):
        event_source.add_handler(handle1)
        event_source.add_handler(handle2)
        event_source.trigger_event()
