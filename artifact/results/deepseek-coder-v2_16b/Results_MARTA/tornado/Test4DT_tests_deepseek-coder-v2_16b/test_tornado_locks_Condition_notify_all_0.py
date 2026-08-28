
import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio

@pytest.mark.asyncio
async def test_valid_input():
    condition = Condition()
    waiter_task = asyncio.create_task(condition.wait())
    await asyncio.sleep(0)  # Give the task a chance to start waiting
    assert not waiter_task.done(), "Waiter should not be done immediately"
    condition.notify()
    await waiter_task
    assert waiter_task.done(), "Waiter should be notified and complete"

@pytest.mark.asyncio
async def test_timeout_case():
    condition = Condition()
    start_time = IOLoop.current().time()
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(condition.wait(), timeout=0.1)
    assert IOLoop.current().time() - start_time >= 0.1, "Time should have passed without notification"

@pytest.mark.asyncio
async def test_invalid_input():
    condition = Condition()
    with pytest.raises(TypeError):
        await condition.wait(timeout="not a valid timeout")
