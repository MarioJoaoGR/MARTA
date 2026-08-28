
import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado.concurrent import Future

def test_event_initialization():
    event = Event()
    assert not event.is_set(), "Event should start un-set"

@pytest.mark.asyncio
async def test_waiter_coroutine():
    event = Event()
    
    async def waiter():
        print("Waiting for event")
        await event.wait()  # This will block until the event is set
        print("Not waiting this time")
        await event.wait()  # Again, wait until the event is set
        print("Done")
    
    async def setter():
        print("About to set the event")
        event.set()  # Set the event to allow waiter coroutine to proceed
    
    await pytest.helpers.run_asyncio(waiter(), setter())
    assert event.is_set(), "Event should be set after setting it"

@pytest.mark.asyncio
async def test_setter_coroutine():
    event = Event()
    
    async def waiter():
        print("Waiting for event")
        await event.wait()  # This will block until the event is set
        print("Not waiting this time")
        await event.wait()  # Again, wait until the event is set
        print("Done")
    
    async def setter():
        print("About to set the event")
        event.set()  # Set the event to allow waiter coroutine to proceed
    
    await pytest.helpers.run_asyncio(waiter(), setter())
    assert event.is_set(), "Event should be set after setting it"

@pytest.mark.asyncio
async def test_event_multiple_waits():
    event = Event()
    
    async def waiter():
        print("First wait")
        await event.wait()  # Wait until the event is set
        print("Second wait")
        await event.wait()  # Again, wait until the event is set
        print("Done waiting")
    
    async def setter():
        print("About to set the event")
        event.set()  # Set the event to allow waiter coroutine to proceed
    
    await pytest.helpers.run_asyncio(waiter(), setter())
    assert event.is_set(), "Event should be set after setting it"
