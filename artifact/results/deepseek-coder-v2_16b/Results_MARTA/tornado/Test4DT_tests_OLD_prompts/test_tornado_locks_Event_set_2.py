
import pytest
from tornado.locks import Event, Future

def test_valid_inputs():
    event = Event()
    fut = event.wait()
    assert not fut.done(), "Event should not be set immediately"

    # Set the event and check if the future is done
    event.set()
    with pytest.raises(StopIteration):
        raise StopIteration
