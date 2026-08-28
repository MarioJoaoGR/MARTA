# Module: tornado.locks
import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
import asyncio
import datetime

@pytest.fixture
def setup_condition():
    condition = Condition()
    loop = asyncio.get_event_loop()
    return condition, loop

@pytest.mark.asyncio
async def test_basic_usage(setup_condition):
    condition, loop = setup_condition

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await asyncio.gather(waiter(), notifier())

    loop.run_until_complete(runner())
    assert True  # Ensure the test completes without errors

@pytest.mark.asyncio
async def test_timeout_absolute(setup_condition):
    condition, loop = setup_condition

    async def waiter():
        timeout = IOLoop.current().time() + 1  # Wait up to 1 second for a notification
        notified = await condition.wait(timeout=timeout)
        assert not notified, "Waiter should time out because no notification is given"

    async def runner():
        await waiter()

    loop.run_until_complete(runner())

@pytest.mark.asyncio
async def test_timeout_relative(setup_condition):
    condition, loop = setup_condition

    async def waiter():
        timeout = datetime.timedelta(seconds=1)  # Wait up to 1 second for a notification
        notified = await condition.wait(timeout=timeout)
        assert not notified, "Waiter should time out because no notification is given"

    async def runner():
        await waiter()

    loop.run_until_complete(runner())

if __name__ == "__main__":
    pytest.main([__file__])
