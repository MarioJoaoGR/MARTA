# Module: tornado.locks
# test_tornado_locks.py
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event
import pytest

@pytest.fixture(scope="module")
def event():
    return Event()

@pytest.mark.asyncio
async def test_event_waiter_setter(event):
    # Define a coroutine that waits for the event to be set
    async def waiter():
        print("Waiting for event")
        await event.wait()  # Blocks until the event is set
        print("Not waiting this time")
        await event.wait()  # Again, blocks until the event is set
        print("Done")

    # Define a coroutine that sets the event
    async def setter():
        print("About to set the event")
        event.set()  # Sets the internal flag of the event to True

    # Define a runner coroutine that runs both waiter and setter concurrently
    async def runner():
        await gen.multi([waiter(), setter()])  # Runs both coroutines in parallel

    # Run the runner coroutine using the current IOLoop
    IOLoop.current().run_sync(runner)

    assert event._value is True  # Ensure the event flag is set after setting

@pytest.mark.asyncio
async def test_event_waiter_after_set(event):
    async def waiter():
        print("Waiting for event")
        await event.wait()  # Should not block since the event is already set
        print("Not waiting this time")
        await event.wait()  # Should not block again
        print("Done")

    async def setter():
        pass  # No need to set the event again, it's already set

    async def runner():
        await gen.multi([waiter(), setter()])

    IOLoop.current().run_sync(runner)

    assert event._value is True  # Ensure the event flag remains set

@pytest.mark.asyncio
async def test_event_clear(event):
    async def waiter():
        print("Waiting for event")
        await event.wait()  # Should block since the event is not set
        print("Not waiting this time")

    async def setter():
        print("About to clear and then set the event")
        event.clear()  # Reset the internal flag to False
        assert event._value is False  # Ensure the event flag is reset
        event.set()  # Set the event again
        assert event._value is True  # Ensure the event flag is now set

    async def runner():
        await gen.multi([waiter(), setter()])

    IOLoop.current().run_sync(runner)

    assert event._value is True  # Ensure the event flag remains set after clearing and setting
