
import pytest
from tornado.locks import Condition
import asyncio

@pytest.fixture
def setup_condition():
    return Condition()

@pytest.mark.asyncio
async def test_waiter_waits(setup_condition):
    condition = setup_condition
    waiter_done = asyncio.Event()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
        nonlocal waiter_done
        waiter_done.set()

    # Start the waiter coroutine
    waiter_task = asyncio.create_task(waiter())

    # Give some time for the waiter to start waiting
    await asyncio.sleep(0.1)

    # Notify the condition
    condition.notify()
    print("Notified")

    # Wait for the waiter to finish
    await waiter_task
    assert waiter_done.is_set(), "Waiter did not complete waiting"

@pytest.mark.asyncio
async def test_waiter_with_timeout(setup_condition):
    condition = setup_condition
    waiter_done = asyncio.Event()

    async def waiter():
        print("I'll wait right here")
        result = await condition.wait(timeout=None)  # None means no timeout
        print("Waited:", "Timeout" if not result else "Notified")
        nonlocal waiter_done
        waiter_done.set()

    # Start the waiter coroutine
    waiter_task = asyncio.create_task(waiter())

    # Give some time for the waiter to start waiting
    await asyncio.sleep(0.1)

    # Notify the condition after a short delay
    await asyncio.sleep(0.2)
    condition.notify()
    print("Notified")

    # Wait for the waiter to finish
    await waiter_task
    assert waiter_done.is_set(), "Waiter did not complete waiting"

@pytest.mark.asyncio
async def test_waiter_with_timeout_absolute(setup_condition):
    condition = setup_condition
    waiter_done = asyncio.Event()

    async def waiter():
        print("I'll wait right here")
        result = await condition.wait(timeout=asyncio.get_event_loop().time() + 0.1)
        print("Waited:", "Timeout" if not result else "Notified")
        nonlocal waiter_done
        waiter_done.set()

    # Start the waiter coroutine
    waiter_task = asyncio.create_task(waiter())

    # Give some time for the waiter to start waiting
    await asyncio.sleep(0.1)

    # Notify the condition after a short delay
    await asyncio.sleep(0.2)
    condition.notify()
    print("Notified")

    # Wait for the waiter to finish
    await waiter_task
    assert waiter_done.is_set(), "Waiter did not complete waiting"
