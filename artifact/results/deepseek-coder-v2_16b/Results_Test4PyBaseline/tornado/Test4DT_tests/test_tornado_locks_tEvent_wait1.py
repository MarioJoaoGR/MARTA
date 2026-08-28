
# Module: tornado.locks
import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event

# Test initialization of the Event class
def test_event_initialization():
    event = Event()
    assert not event._value, "Event should be initialized with _value set to False"
    assert len(event._waiters) == 0, "Waiters list should be empty upon initialization"

# Test the wait method without timeout
@gen.coroutine
def test_event_wait_without_timeout():
    event = Event()
    
    def waiter():
        return event.wait()
    
    # Start the waiter coroutine and yield it to ensure it's waiting
    waiter_future = IOLoop.current().add_callback(lambda: IOLoop.current().create_future())
    with pytest.raises(gen.TimeoutError):  # Corrected from gen.ReturnFuture to gen.TimeoutError
        yield waiter_future  # This should raise a TimeoutError because the event is not set yet
    
    # Set the event and check if the waiter coroutine resumes
    event.set()
    yield waiter_future  # The future should now be done since the event has been set

# Test the wait method with timeout
@gen.coroutine
def test_event_wait_with_timeout():
    event = Event()
    
    def waiter():
        return event.wait(timeout=0.1)  # Wait for a short period
    
    # Start the waiter coroutine and yield it to ensure it's waiting with timeout
    waiter_future = IOLoop.current().add_callback(lambda: IOLoop.current().create_future())
    with pytest.raises(gen.TimeoutError):  # Corrected from gen.ReturnFuture to gen.TimeoutError
        yield waiter_future  # This should raise a TimeoutError because the event is not set yet and the timeout is very short
    
    # Set the event and check if the waiter coroutine resumes without raising an error
    event.set()
    yield waiter_future  # The future should now be done since the event has been set

# Test the wait method with immediate return due to already being set
def test_event_wait_already_set():
    event = Event()
    event.set()
    
    fut = event.wait()
    assert isinstance(fut, gen.Future)
    assert fut.done()
    assert fut.result() is None  # The result should be None since the event was set

# Test the wait method with timeout and immediate return due to already being set
def test_event_wait_timeout_already_set():
    event = Event()
    event.set()
    
    fut = event.wait(timeout=0.1)
    assert isinstance(fut, gen.Future)
    assert fut.done()
    assert fut.result() is None  # The result should be None since the event was set

# Test the wait method with timeout and ensure it raises TimeoutError after the specified duration
@gen.coroutine
def test_event_wait_with_timeout_error():
    event = Event()
    
    def waiter():
        return event.wait(timeout=0.1)  # Wait for a short period with timeout
    
    # Start the waiter coroutine and yield it to ensure it's waiting with timeout
    waiter_future = IOLoop.current().add_callback(lambda: IOLoop.current().create_future())
    start_time = IOLoop.current().time()
    with pytest.raises(gen.TimeoutError):  # Corrected from gen.ReturnFuture to gen.TimeoutError
        yield waiter_future  # This should raise a TimeoutError because the event is not set yet and the timeout is very short
    
    # Check if the elapsed time is close to the specified timeout duration
    end_time = IOLoop.current().time()
    assert abs(end_time - start_time - 0.1) < 0.02, "Timeout should be approximately equal to the specified duration"

# Run all tests
if __name__ == "__main__":
    pytest.main([__file__])
