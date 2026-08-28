# Module: tornado.locks
import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado import gen

# Test initialization of Event instance
def test_event_initialization():
    event = Event()
    assert not event.is_set(), "Event should be initialized as not set"

# Test setting the event and waiting coroutine
@gen.coroutine
def test_event_wait_and_set():
    event = Event()
    
    # Define a coroutine that waits for the event to be set
    @gen.coroutine
    def waiter():
        print("Waiting for event")
        yield event.wait()  # Wait until the event is set
        print("Not waiting this time")
        yield event.wait()  # Return immediately if the event was already set
        print("Done")
    
    # Define a coroutine that sets the event
    @gen.coroutine
    def setter():
        print("About to set the event")
        event.set()  # Set the event so that waiter can proceed
    
    # Run both coroutines in parallel
    yield gen.multi([waiter(), setter()])
    
    assert event.is_set(), "Event should be set after setting it"

# Test waiting when the event is already set
@gen.coroutine
def test_event_already_set():
    event = Event()
    
    # Set the event immediately
    event.set()
    
    @gen.coroutine
    def waiter():
        print("Waiting for event")
        yield event.wait()  # Should return immediately as the event is already set
        print("Not waiting this time")
        yield event.wait()  # Should also return immediately
        print("Done")
    
    @gen.coroutine
    def setter():
        pass  # No need to set the event again, it's already set
    
    yield gen.multi([waiter(), setter()])

# Test multiple coroutines waiting for the same event
@gen.coroutine
def test_multiple_waiters():
    event = Event()
    
    @gen.coroutine
    def waiter1():
        print("Waiter 1: Waiting for event")
        yield event.wait()
        print("Waiter 1: Not waiting this time")
        yield event.wait()
        print("Waiter 1: Done")
    
    @gen.coroutine
    def waiter2():
        print("Waiter 2: Waiting for event")
        yield event.wait()
        print("Waiter 2: Not waiting this time")
        yield event.wait()
        print("Waiter 2: Done")
    
    @gen.coroutine
    def setter():
        print("About to set the event")
        event.set()
    
    yield gen.multi([waiter1(), waiter2(), setter()])

# Run all tests
if __name__ == "__main__":
    pytest.main()
