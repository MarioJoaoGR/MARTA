
import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio
import datetime

@pytest.fixture
def condition():
    return Condition()

@pytest.mark.asyncio
async def test_valid_input(condition):
    waiter_done = asyncio.Event()
    
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
        nonlocal waiter_done
        waiter_done.set()

    # Run the waiter coroutine in a separate task
    waiter_task = asyncio.create_task(waiter())
    
    # Give some time for the waiter to start waiting
    await asyncio.sleep(0.1)
    
    # Notify the waiter
    condition.notify()
    
    # Wait for the waiter to complete
    await waiter_task
    
    assert waiter_done.is_set(), "Waiter did not receive notification"

@pytest.mark.asyncio
async def test_timeout(condition):
    async def waiter():
        print("I'll wait right here")
        notified = await condition.wait(timeout=datetime.timedelta(seconds=1))
        assert not notified, "Waiter should time out"
        print("I'm done waiting")

    # Run the waiter coroutine in a separate task
    waiter_task = asyncio.create_task(waiter())
    
    # Give some time for the waiter to start waiting
    await asyncio.sleep(0.1)
    
    # Wait for the waiter to complete (it should timeout and not reach here)
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(waiter_task, timeout=1)

@pytest.mark.asyncio
async def test_invalid_input(condition):
    with pytest.raises(TypeError):
        condition.notify("not an integer")  # Notify with non-integer value should raise TypeError
