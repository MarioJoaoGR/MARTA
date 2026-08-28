
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
async def test_event_waiter_after_clear(event):
    """Test that a waiter coroutine blocks correctly after the event is cleared."""
    async def waiter():
        print("Waiting for event")
        with pytest.raises(Exception) as excinfo:  # Expect an exception since the event is not set yet
            await event.wait()
        assert str(excinfo.value) == "Event has not been set"  # Check if the exception message matches expected
        print("Not waiting this time")

    async def setter():
        print("About to clear and then set the event")
        event.clear()  # Reset the internal flag to False
        assert event._value is False  # Ensure the event flag is reset
        await gen.sleep(0.1)  # Give some time for waiter to react to the change
        event.set()  # Set the event again
        assert event._value is True  # Ensure the event flag is now set

    async def runner():
        await gen.multi([waiter(), setter()])

    IOLoop.current().run_sync(runner)

    assert event._value is True  # Ensure the event flag remains set after clearing and setting

@pytest.mark.asyncio
async def test_event_multiple_waiters(event):
    """Test that multiple waiters correctly block when the event is not set."""
    async def waiter1():
        print("Waiter 1 waiting for event")
        with pytest.raises(Exception) as excinfo:
            await event.wait()
        assert str(excinfo.value) == "Event has not been set"
        print("Waiter 1 not waiting this time")

    async def waiter2():
        print("Waiter 2 waiting for event")
        with pytest.raises(Exception) as excinfo:
            await event.wait()
        assert str(excinfo.value) == "Event has not been set"
        print("Waiter 2 not waiting this time")

    async def setter():
        print("About to clear and then set the event")
        event.clear()  # Reset the internal flag to False
        assert event._value is False  # Ensure the event flag is reset
        await gen.sleep(0.1)  # Give some time for waiters to react to the change
        event.set()  # Set the event again
        assert event._value is True  # Ensure the event flag is now set

    async def runner():
        await gen.multi([waiter1(), waiter2(), setter()])

    IOLoop.current().run_sync(runner)

    assert event._value is True  # Ensure the event flag remains set after clearing and setting

@pytest.mark.asyncio
async def test_event_clear_and_set_race_condition(event):
    """Test a race condition where clear, set, and wait operations are interleaved."""
    async def waiter():
        print("Waiting for event")
        with pytest.raises(Exception) as excinfo:
            await event.wait()
        assert str(excinfo.value) == "Event has not been set"
        print("Not waiting this time")

    async def setter():
        print("About to clear and then set the event")
        event.clear()  # Reset the internal flag to False
        assert event._value is False  # Ensure the event flag is reset
        await gen.sleep(0.1)  # Give some time for waiter to react to the change
        event.set()  # Set the event again
        assert event._value is True  # Ensure the event flag is now set

    async def runner():
        tasks = [waiter(), setter()]
        await gen.multi(tasks)

    IOLoop.current().run_sync(runner)

    assert event._value is True  # Ensure the event flag remains set after clearing and setting
