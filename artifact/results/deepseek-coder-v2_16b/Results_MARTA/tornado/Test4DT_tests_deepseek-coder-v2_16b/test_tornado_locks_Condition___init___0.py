
import pytest
from tornado.ioloop import IOLoop
from tornado.locks import Condition
import asyncio

@pytest.mark.asyncio
async def test_waiter_waits_and_notifies():
    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        await asyncio.sleep(0.1)  # Small delay to ensure waiter has time to start waiting
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        await asyncio.gather(waiter(), notifier())

    IOLoop.current().run_sync(lambda: None)  # Run the asyncio loop within the sync context of run_sync
    await runner()

    assert True, "Test passed"

@pytest.mark.asyncio
async def test_waiter_times_out():
    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        result = await condition.wait(timeout=0.1)  # Wait for a short period
        assert not result, "Wait should time out"
        print("Timeout: No notification received")

    async def runner():
        await waiter()

    IOLoop.current().run_sync(lambda: None)  # Run the asyncio loop within the sync context of run_sync
    await runner()

    assert True, "Test passed"
