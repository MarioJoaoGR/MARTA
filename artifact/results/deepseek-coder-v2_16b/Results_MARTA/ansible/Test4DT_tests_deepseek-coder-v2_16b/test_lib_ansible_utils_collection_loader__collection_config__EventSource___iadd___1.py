
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource



def test_invalid_input():
    event_source = _EventSource()
    handle1 = 'not callable'
    handle2 = lambda: print('Handler 2')
    
    # Add an invalid handler
    with pytest.raises(ValueError):
        event_source += handle1