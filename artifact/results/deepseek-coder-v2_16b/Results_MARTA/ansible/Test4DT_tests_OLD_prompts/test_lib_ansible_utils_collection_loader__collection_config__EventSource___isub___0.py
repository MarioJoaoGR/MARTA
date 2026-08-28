
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource


def test_edge_cases():
    event_source = _EventSource()

    # Test adding None as a handler
    with pytest.raises(AttributeError):
        event_source.add_handler(None)
