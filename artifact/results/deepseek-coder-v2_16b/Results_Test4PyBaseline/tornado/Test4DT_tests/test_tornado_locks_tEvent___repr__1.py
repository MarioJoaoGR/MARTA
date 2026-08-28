
import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event

# Test the initialization of the Event class
def test_event_initialization():
    event = Event()
    assert not event._value, "Event should be initialized with _value set to False"
    assert len(event._waiters) == 0, "Waiters set should be empty initially"

# Test the wait method when the event is already set
def test_event_wait_when_set():
    event = Event()
    event.set()
    loop = IOLoop.current()
    
    async def test():
        await event.wait()
    
    future = loop.run_sync(test)
    assert future is None, "Wait should return immediately when the event is set"

# Test the wait method with a timeout
def test_event_wait_with_timeout():
    event = Event()
    loop = IOLoop.current()
    
    async def test():
        with pytest.raises(gen.TimeoutError):
            await event.wait(timeout=0.1)
    
    future = loop.run_sync(test)

# Test the __repr__ method when the event is set
def test_event_repr_when_set():
    event = Event()
    event.set()
    assert repr(event) == "<Event set>", "The representation should indicate that the event is set"

# Test the __repr__ method when the event is not set
def test_event_repr_when_not_set():
    event = Event()
    assert repr(event) == "<Event clear>", "The representation should indicate that the event is not set"
