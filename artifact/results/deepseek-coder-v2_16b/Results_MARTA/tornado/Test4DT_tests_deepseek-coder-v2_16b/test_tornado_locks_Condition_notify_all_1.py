
import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_valid_input():
    condition = Condition()
    waiter_task = asyncio.create_task(condition.wait())
    await asyncio.sleep(0)  # Allow time for the waiter to start waiting
    assert not waiter_task.done(), "Waiter should not be done immediately"
    condition.notify()
    await asyncio.sleep(0)  # Allow time for the notification to be processed
    assert waiter_task.done(), "Waiter should be notified and done after notify"

@pytest.mark.asyncio
async def test_timeout_case():
    condition = Condition()
    start_time = IOLoop.current().time()
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(condition.wait(timeout=start_time + 1), timeout=0.5)

@pytest.mark.asyncio
async def test_invalid_input():
    condition = Condition()
    with pytest.raises(TypeError):
        await condition.wait(timeout="not a valid type")
