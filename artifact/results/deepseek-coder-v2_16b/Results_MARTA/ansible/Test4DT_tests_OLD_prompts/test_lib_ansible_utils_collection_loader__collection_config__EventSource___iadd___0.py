
import pytest
from ansible.utils.collection_loader._collection_config import _EventSource


def test_trigger_event():
    event_source = _EventSource()

    called_handlers = []

    def handle1():
        called_handlers.append(handle1)

    def handle2():
        called_handlers.append(handle2)

    event_source += handle1
    event_source += handle2

    with pytest.raises(AttributeError):
        event_source.trigger_event()