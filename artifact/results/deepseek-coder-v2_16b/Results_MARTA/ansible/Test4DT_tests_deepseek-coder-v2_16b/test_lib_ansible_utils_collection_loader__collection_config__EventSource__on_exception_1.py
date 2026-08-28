
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource

def test_edge_case():
    event_source = _EventSource()
    
    def handle2():
        pass
    
    with pytest.raises(AttributeError):
        event_source.add_handler(handle2)

def test_invalid_input():
    event_source = _EventSource()
    
    with pytest.raises(AttributeError):
        event_source.add_handler(None)
