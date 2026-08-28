
# Module: tornado.locks
import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event
from concurrent.futures import Future  # Importing from concurrent.futures instead of directly using Future
import time  # Importing the actual time module

# Test initialization of the Event class
def test_event_initialization():
    event = Event()
    assert not event._value, "Event should be initialized with _value set to False"
    assert len(event._waiters) == 0, "Waiters set should be empty initially"

# Test setting the event and waking up waiters
@gen.coroutine
def test_set_event():
    event = Event()
    
    # Create a future to simulate waiting coroutines
    waiter1 = Future()
    waiter2 = Future()
    
    # Add futures to the waiters set
    event._waiters.add(waiter1)
    event._waiters.add(waiter2)
    
    # Set the event, which should wake up all waiters
    event.set()
    
    # Check that both futures are done after setting the event
    assert waiter1.done(), "Waiter 1 should be woken up by the event"
    assert waiter2.done(), "Waiter 2 should be woken up by the event"
    assert event._value, "Event value should be set to True after calling set()"

# Test waiting for an event that is already set
@gen.coroutine
def test_wait_event():
    event = Event()
    
    # Set the event immediately
    event.set()
    
    # Wait for the event, which should not block since it's already set
    yield event.wait()
    assert True, "Waiting on an already set event should not block"

# Test waiting with a timeout for an event that is not yet set
@gen.coroutine
def test_wait_timeout():
    event = Event()
    
    # Start waiting with a timeout of 0.1 seconds
    start_time = time.time()
    with pytest.raises(TimeoutError):
        yield event.wait(timeout=0.1)
    assert time.time() - start_time >= 0.1, "Waiting with a timeout should respect the timeout duration"

# Test clearing and setting the event multiple times
@gen.coroutine
def test_clear_and_set():
    event = Event()
    
    # Set the event immediately
    event.set()
    
    # Wait for the event, which should not block since it's already set
    yield event.wait()
    
    # Clear the event and wait again with a timeout of 0.1 seconds
    event.clear()
    start_time = time.time()
    with pytest.raises(TimeoutError):
        yield event.wait(timeout=0.1)
    assert time.time() - start_time >= 0.1, "Waiting after clearing the event should respect the timeout duration"

# Test multiple waiters and setting the event
@gen.coroutine
def test_multiple_waiters():
    event = Event()
    
    # Create two futures to simulate waiting coroutines
    waiter1 = Future()
    waiter2 = Future()
    
    # Add futures to the waiters set
    event._waiters.add(waiter1)
    event._waiters.add(waiter2)
    
    # Set the event, which should wake up both waiters
    event.set()
    
    # Check that both futures are done after setting the event
    assert waiter1.done(), "Waiter 1 should be woken up by the event"
    assert waiter2.done(), "Waiter 2 should be woken up by the event"
    assert event._value, "Event value should be set to True after calling set()"

# Run all tests in an async IOLoop
if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v", "--asyncio-mode=auto"])
